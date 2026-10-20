"""Connect to Google Docs and Confluence using whatever this machine has. Each target picks one of:

  api     call the API directly (Google: one-time OAuth login; Confluence: email + API token) — no MCP needed
  mcp     go through an MCP server: an HTTP URL (MCP Manager or any gateway) or a stdio server command (uvx/npx ...)
  manual  no automatic publishing; the publish scripts print upload instructions for the Word file
  auto    (default) try api -> mcp -> manual

Configuration: ~/.config/rsd-kit/config.json (sample: rsd-kit/templates/config.example.json) or environment variables (take precedence):
  RSD_GOOGLE_VIA, RSD_GOOGLE_MCP, RSD_GOOGLE_OAUTH_CLIENT
  RSD_CONFLUENCE_VIA, RSD_CONFLUENCE_MCP, ATLASSIAN_SITE, ATLASSIAN_EMAIL, ATLASSIAN_API_TOKEN
  MCP_GATEWAY (used for both targets when RSD_*_MCP is not set)

    python3 rsd-kit/scripts/connect.py               # show which method each target will use
    python3 rsd-kit/scripts/connect.py google-login  # one-time Google login for the api method (opens a browser)
"""
import base64
import hashlib
import http.server
import json
import os
import re
import secrets
import subprocess
import sys
import threading
import time
import urllib.parse
import urllib.request
import uuid
import webbrowser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mcp as mcplib  # noqa: E402

CONF_DIR = os.path.expanduser(os.environ.get('RSD_CONFIG_DIR', '~/.config/rsd-kit'))
DEFAULT_GATEWAY = 'http://127.0.0.1:7717/mcp'


def config():
    path = os.path.join(CONF_DIR, 'config.json')
    c = json.load(open(path)) if os.path.exists(path) else {}
    g, f = c.setdefault('google', {}), c.setdefault('confluence', {})
    env = os.environ.get
    g['via'] = env('RSD_GOOGLE_VIA') or g.get('via', 'auto')
    g['mcp'] = env('RSD_GOOGLE_MCP') or env('MCP_GATEWAY') or g.get('mcp') or DEFAULT_GATEWAY
    g['oauth_client'] = os.path.expanduser(env('RSD_GOOGLE_OAUTH_CLIENT') or g.get('oauth_client') or os.path.join(CONF_DIR, 'google-oauth-client.json'))
    f['via'] = env('RSD_CONFLUENCE_VIA') or f.get('via', 'auto')
    f['mcp'] = env('RSD_CONFLUENCE_MCP') or env('MCP_GATEWAY') or f.get('mcp') or DEFAULT_GATEWAY
    for k, e in [('site', 'ATLASSIAN_SITE'), ('email', 'ATLASSIAN_EMAIL'), ('api_token', 'ATLASSIAN_API_TOKEN')]:
        f[k] = env(e) or f.get(k)
    if f.get('site') and not f['site'].startswith('http'):
        f['site'] = f'https://{f["site"]}'
    return c


def _mcp(spec, need):
    """Connect to an MCP server if it is available and has the required tools; otherwise (None, reason)."""
    if spec.startswith('http') and not mcplib.reachable(spec):
        return None, f'cannot reach {spec}'
    try:
        m = mcplib.connect(spec)
    except Exception as e:
        return None, f'cannot connect to MCP ({str(e)[:120]})'
    missing = [t for t in need if not m.has(t)]
    return (None, f'MCP {spec} lacks tools {missing}') if missing else (m, f'MCP {spec}')


def _http(method, url, headers=None, data=None, timeout=300):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            return json.loads(raw) if raw and r.headers.get('Content-Type', '').startswith('application/json') else raw
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'{method} {url} -> {e.code}: {e.read().decode("utf-8", "ignore")[:500]}')


def _multipart(fields):
    """fields: [(name, filename|None, content-type, bytes)] -> (body, content-type)."""
    b = uuid.uuid4().hex
    out = b''
    for name, filename, ctype, data in fields:
        disp = f'form-data; name="{name}"' + (f'; filename="{filename}"' if filename else '')
        out += f'--{b}\r\nContent-Disposition: {disp}\r\nContent-Type: {ctype}\r\n\r\n'.encode() + data + b'\r\n'
    return out + f'--{b}--\r\n'.encode(), f'multipart/form-data; boundary={b}'


# =========================================================================== Google
GOOGLE_TOOLS = ['import_to_google_doc', 'set_drive_file_permissions']
GOOGLE_SCOPE = 'https://www.googleapis.com/auth/drive.file'


class GoogleAPI:
    """Drive REST API with the user's own OAuth (Desktop-type OAuth client, drive.file scope)."""
    via = 'api'

    def __init__(self, cfg):
        self.client = json.load(open(cfg['oauth_client']))
        self.client = self.client.get('installed') or self.client.get('web')
        self.token_path = os.path.join(CONF_DIR, 'google-token.json')
        self._access = None

    def login(self):
        verifier = secrets.token_urlsafe(64)
        challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip('=')
        got = {}

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                got.update(urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query))
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write(b'Login complete, you can return to the terminal.')

            def log_message(self, *a):
                pass
        srv = http.server.HTTPServer(('127.0.0.1', 0), Handler)
        redirect = f'http://127.0.0.1:{srv.server_port}'
        url = self.client['auth_uri'] + '?' + urllib.parse.urlencode({
            'client_id': self.client['client_id'], 'redirect_uri': redirect, 'response_type': 'code', 'scope': GOOGLE_SCOPE,
            'access_type': 'offline', 'prompt': 'consent', 'code_challenge': challenge, 'code_challenge_method': 'S256'})
        print('Open this URL to sign in to Google:\n' + url)
        webbrowser.open(url)
        threading.Thread(target=srv.handle_request, daemon=True).start()
        for _ in range(300):
            if got:
                break
            time.sleep(1)
        srv.server_close()
        if 'code' not in got:
            sys.exit('No Google authorization code received (timed out after 5 minutes or access was denied)')
        tok = _http('POST', self.client['token_uri'], {'Content-Type': 'application/x-www-form-urlencoded'}, urllib.parse.urlencode({
            'code': got['code'][0], 'client_id': self.client['client_id'], 'client_secret': self.client.get('client_secret', ''),
            'redirect_uri': redirect, 'grant_type': 'authorization_code', 'code_verifier': verifier}).encode())
        os.makedirs(CONF_DIR, exist_ok=True)
        json.dump(tok, open(self.token_path, 'w'))
        os.chmod(self.token_path, 0o600)
        print('Google login saved:', self.token_path)

    def _token(self):
        if self._access:
            return self._access
        if not os.path.exists(self.token_path):
            raise RuntimeError('Not logged in to Google — run: python3 rsd-kit/scripts/connect.py google-login')
        tok = json.load(open(self.token_path))
        r = _http('POST', self.client['token_uri'], {'Content-Type': 'application/x-www-form-urlencoded'}, urllib.parse.urlencode({
            'refresh_token': tok['refresh_token'], 'client_id': self.client['client_id'],
            'client_secret': self.client.get('client_secret', ''), 'grant_type': 'refresh_token'}).encode())
        self._access = r['access_token']
        return self._access

    def import_docx(self, path, title, folder='root'):
        meta = {'name': title, 'mimeType': 'application/vnd.google-apps.document'} | ({'parents': [folder]} if folder != 'root' else {})
        b = uuid.uuid4().hex
        body = (f'--{b}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n{json.dumps(meta)}\r\n'
                f'--{b}\r\nContent-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document\r\n\r\n').encode() \
            + open(path, 'rb').read() + f'\r\n--{b}--\r\n'.encode()
        r = _http('POST', 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id',
                  {'Authorization': 'Bearer ' + self._token(), 'Content-Type': f'multipart/related; boundary={b}'}, body)
        return r['id']

    def share(self, doc_id, role):
        _http('POST', f'https://www.googleapis.com/drive/v3/files/{doc_id}/permissions',
              {'Authorization': 'Bearer ' + self._token(), 'Content-Type': 'application/json'},
              json.dumps({'type': 'anyone', 'role': role}).encode())


class GoogleMCP:
    """workspace-mcp server (taylorwilsdon/google_workspace_mcp) over HTTP or stdio."""
    via = 'mcp'

    def __init__(self, m):
        self.m = m

    def import_docx(self, path, title, folder='root'):
        data = open(path, 'rb').read()      # sent as base64: the server only reads files from its own folder
        txt = self.m.tool('import_to_google_doc', {'file_name': title, 'source_format': 'docx', 'folder_id': folder,
                                                   'base64_content': base64.b64encode(data).decode(),
                                                   'base64_sha256': hashlib.sha256(data).hexdigest()})
        return re.search(r'Document ID: (\S+)', txt).group(1)

    def share(self, doc_id, role):
        self.m.tool('set_drive_file_permissions', {'file_id': doc_id, 'link_sharing': role})


def google(cfg=None):
    """-> (backend, or None for manual; description)."""
    g = (cfg or config())['google']
    why = []
    if g['via'] in ('auto', 'api'):
        if os.path.exists(g['oauth_client']):
            return GoogleAPI(g), 'API (your OAuth login)'
        why.append(f'api: no OAuth client at {g["oauth_client"]}')
    if g['via'] in ('auto', 'mcp'):
        m, msg = _mcp(g['mcp'], GOOGLE_TOOLS)
        if m:
            return GoogleMCP(m), msg
        why.append('mcp: ' + msg)
    return None, 'manual — ' + '; '.join(why or [f'via={g["via"]}'])


# =========================================================================== Confluence
ROVO_TOOLS = ['getAccessibleAtlassianResources', 'createConfluenceContent', 'updateConfluenceContent', 'getConfluenceContent', 'executeRead', 'executeWrite']


class ConfluenceAPI:
    """Confluence Cloud REST API (v2, plus v1 for attachments), email + API token auth. Content in storage format."""
    via, dialect = 'api', 'storage'

    def __init__(self, f):
        self.site = f['site'].rstrip('/')
        self.auth = 'Basic ' + base64.b64encode(f'{f["email"]}:{f["api_token"]}'.encode()).decode()

    def _j(self, method, path, body=None):
        h = {'Authorization': self.auth, 'Accept': 'application/json'}
        if body is not None:
            h['Content-Type'] = 'application/json'
        return _http(method, self.site + path, h, json.dumps(body).encode() if body is not None else None)

    def space(self, key_or_id):
        if key_or_id.isdigit():
            s = self._j('GET', f'/wiki/api/v2/spaces/{key_or_id}')
        else:
            r = self._j('GET', '/wiki/api/v2/spaces?keys=' + urllib.parse.quote(key_or_id))['results']
            s = r[0] if r else None
        return s and {'id': s['id'], 'key': s['key'], 'name': s['name'], 'homepageId': s.get('homepageId'), 'instructions': ''}

    def find_page(self, space, title):
        r = self._j('GET', f'/wiki/api/v2/pages?space-id={space["id"]}&status=current&title=' + urllib.parse.quote(title))['results']
        return r[0]['id'] if r else None

    def create_page(self, space, parent, title, body):
        r = self._j('POST', '/wiki/api/v2/pages', {'spaceId': space['id'], 'status': 'current', 'title': title,
                                                     'parentId': parent or space.get('homepageId'),
                                                     'body': {'representation': 'storage', 'value': body}})
        return r['id']

    def upload(self, page_id, path):
        body, ctype = _multipart([('file', os.path.basename(path), 'image/png', open(path, 'rb').read()), ('minorEdit', None, 'text/plain', b'true')])
        _http('PUT', f'{self.site}/wiki/rest/api/content/{page_id}/child/attachment',      # PUT = create or update
              {'Authorization': self.auth, 'X-Atlassian-Token': 'nocheck', 'Content-Type': ctype}, body)
        return os.path.basename(path)

    def update_page(self, page_id, body, message):
        p = self._j('GET', f'/wiki/api/v2/pages/{page_id}')
        self._j('PUT', f'/wiki/api/v2/pages/{page_id}', {'id': page_id, 'status': 'current', 'title': p['title'],
                                                          'body': {'representation': 'storage', 'value': body},
                                                          'version': {'number': p['version']['number'] + 1, 'message': message}})

    def read_body(self, page_id):
        return self._j('GET', f'/wiki/api/v2/pages/{page_id}?body-format=storage')['body']['storage']['value']

    def url(self, page_id):
        return f'{self.site}/wiki/pages/viewpage.action?pageId={page_id}'


class ConfluenceRovo:
    """Atlassian Rovo MCP (mcp.atlassian.com) over HTTP or stdio (npx mcp-remote). Content in HTML (adf dialect)."""
    via, dialect = 'mcp', 'adf'

    def __init__(self, m, site=None):
        self.m = m
        res = [r for r in m.tool_json('getAccessibleAtlassianResources', {})['data']['resources']
               if any(p['id'] == 'confluence' for p in r['products'])]
        res = [r for r in res if not site or site.rstrip('/').split('//')[-1] in r['url']] or res
        if not res:
            raise RuntimeError('the Atlassian account behind this MCP server has no Confluence access')
        self.cid, self.site = res[0]['cloudId'], res[0]['url']

    def _read(self, name, inputs):
        return self.m.tool_json('executeRead', {'name': name, 'cloudId': self.cid, 'inputs': {'cloudId': self.cid} | inputs})['data']

    def space(self, key_or_id):
        r = self._read('listConfluenceSpaces', {('ids' if key_or_id.isdigit() else 'keys'): [key_or_id]})['results']
        if not r:
            return None
        info = self._read('getConfluenceSpace', {'spaceIdOrKey': r[0]['key']})
        return {'id': r[0]['id'], 'key': r[0]['key'], 'name': r[0]['name'], 'homepageId': r[0].get('homepageId'),
                'instructions': info.get('spaceInstructions') or ''}

    def find_page(self, space, title):            # CQL search misses pages in personal spaces -> list pages of the space
        cursor = None
        while True:
            d = self._read('listConfluenceContent', {'type': 'page', 'spaceId': space['id'], 'limit': 250} | ({'cursor': cursor} if cursor else {}))
            hit = next((p['id'] for p in d.get('results', []) if p.get('title') == title), None)
            cursor = d.get('cursor') or d.get('nextCursor')
            if hit or not cursor:
                return hit

    def create_page(self, space, parent, title, body):
        r = self.m.tool_json('createConfluenceContent', {'cloudId': self.cid, 'contentType': 'page', 'title': title,
                                                        'parent': {'spaceId': space['id']} | ({'parentContentId': parent} if parent else {}),
                                                        'body': {'format': 'html', 'value': body}})['data']
        if not r.get('ok'):
            raise RuntimeError('page creation failed: ' + json.dumps(r, ensure_ascii=False)[:600])
        return r['content']['id']

    def upload(self, page_id, path):
        d = self.m.tool_json('executeWrite', {'name': 'createConfluenceAttachment', 'cloudId': self.cid, 'inputs': {
            'cloudId': self.cid, 'contentId': page_id, 'localFilePath': path, 'fileSize': os.path.getsize(path)}})['data']
        out = subprocess.run(d['uploadCommand'], shell=True, capture_output=True, text=True).stdout   # short-lived token, never printed
        j = json.loads(out)
        return (j['results'][0] if 'results' in j else j)['fileId']

    def update_page(self, page_id, body, message):
        snap = self.m.tool_json('getConfluenceContent', {'cloudId': self.cid, 'content_id': page_id, 'detail': 'summary'})['data']['snapshotToken']
        r = self.m.tool_json('updateConfluenceContent', {'cloudId': self.cid, 'contentId': page_id, 'snapshotToken': snap,   # no title: it triggers "title exists"
                                                        'body': {'format': 'html', 'value': body}, 'versionMessage': message})['data']
        if not r.get('ok'):
            raise RuntimeError('page update failed: ' + json.dumps(r, ensure_ascii=False)[:600])

    def read_body(self, page_id):
        return self.m.tool_json('getConfluenceContent', {'cloudId': self.cid, 'content_id': page_id, 'detail': 'full', 'format': 'html'})['data']['body']['value']

    def url(self, page_id):
        return f'{self.site}/wiki/pages/viewpage.action?pageId={page_id}'


def confluence(cfg=None):
    f = (cfg or config())['confluence']
    why = []
    if f['via'] in ('auto', 'api'):
        if f.get('site') and f.get('email') and f.get('api_token'):
            return ConfluenceAPI(f), f'API ({f["site"]}, {f["email"]})'
        why.append('api: site/email/api_token not set')
    if f['via'] in ('auto', 'mcp'):
        m, msg = _mcp(f['mcp'], ROVO_TOOLS)
        if m:
            try:
                return ConfluenceRovo(m, f.get('site')), msg
            except Exception as e:
                msg = str(e)[:200]
        why.append('mcp: ' + msg)
    return None, 'manual — ' + '; '.join(why or [f'via={f["via"]}'])


if __name__ == '__main__':
    if sys.argv[1:] == ['google-login']:
        GoogleAPI(config()['google']).login()
        sys.exit(0)
    c = config()
    gb, gm = google(c)
    print('Google Docs :', gm)
    cb, cm = confluence(c)
    print('Confluence  :', cm)
    if not gb or not cb:
        print('Setup: rsd-kit/README.md, section "Connections".')
