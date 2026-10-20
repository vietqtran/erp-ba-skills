"""Minimal MCP client with two transports:

- HTTP (streamable HTTP): a URL, e.g. the MCP Manager gateway http://127.0.0.1:7717/mcp or any other gateway.
- stdio: a command that starts the server, e.g. "uvx workspace-mcp --single-user --tools drive" or
  "npx -y mcp-remote https://mcp.atlassian.com/v2/mcp". The server is started on demand and stopped on exit.

Tool names may be given in full or by suffix (gateways prefix tools with "<server>__").

    python3 mcp.py list <url|command> [keyword ...]
    python3 mcp.py call <url|command> <tool> '<json>'
"""
import atexit
import json
import shlex
import subprocess
import sys
import threading
import urllib.error
import urllib.request


class _Base:
    def _init(self):
        self.n, self._tools = 0, None
        self.request('initialize', {'protocolVersion': '2025-03-26', 'capabilities': {},
                                    'clientInfo': {'name': 'rsd-kit', 'version': '2'}})
        self.notify('notifications/initialized')

    def request(self, method, params=None):
        self.n += 1
        r = self._send({'jsonrpc': '2.0', 'id': self.n, 'method': method, 'params': params or {}})
        if r and 'error' in r:
            raise RuntimeError(json.dumps(r['error'], ensure_ascii=False))
        return (r or {}).get('result')

    def tools(self):
        if self._tools is None:
            self._tools = self.request('tools/list')['tools']
        return self._tools

    def has(self, name):
        return any(t['name'] == name or t['name'].endswith('__' + name) for t in self.tools())

    def resolve(self, name):
        for t in self.tools():
            if t['name'] == name or t['name'].endswith('__' + name):
                return t['name']
        raise RuntimeError(f'MCP server has no tool "{name}"')

    def tool(self, name, args, retries=2):
        """Call a tool and return its text; a tool error raises RuntimeError (after `retries` retries)."""
        full = self.resolve(name)
        for attempt in range(retries + 1):
            r = self.request('tools/call', {'name': full, 'arguments': args})
            txt = ''.join(c.get('text', '') for c in r.get('content', []))
            if not r.get('isError'):
                return txt
            if attempt == retries:
                raise RuntimeError(f'{full}: {txt[:800]}')

    def tool_json(self, name, args):
        return json.loads(self.tool(name, args))


class HttpMCP(_Base):
    def __init__(self, url):
        self.url, self.sid = url, None
        self._init()

    def notify(self, method):
        self._send({'jsonrpc': '2.0', 'method': method})

    def _send(self, body):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json, text/event-stream'}
        if self.sid:
            headers['Mcp-Session-Id'] = self.sid
        req = urllib.request.Request(self.url, data=json.dumps(body).encode(), headers=headers, method='POST')
        with urllib.request.urlopen(req, timeout=600) as resp:
            self.sid = resp.headers.get('Mcp-Session-Id') or self.sid
            raw, ctype = resp.read().decode(), resp.headers.get('Content-Type', '')
        if not raw.strip():
            return None
        if 'event-stream' in ctype:
            for line in raw.splitlines():
                if line.startswith('data:'):
                    msg = json.loads(line[5:].strip())
                    if msg.get('id') == body.get('id'):
                        return msg
            return None
        return json.loads(raw)


class StdioMCP(_Base):
    def __init__(self, command, timeout=600):
        self.timeout = timeout
        self.p = subprocess.Popen(shlex.split(command), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.DEVNULL, text=True, bufsize=1)
        atexit.register(self.close)
        self._init()

    def notify(self, method):
        self.p.stdin.write(json.dumps({'jsonrpc': '2.0', 'method': method}) + '\n')
        self.p.stdin.flush()

    def _send(self, body):
        self.p.stdin.write(json.dumps(body) + '\n')
        self.p.stdin.flush()
        result = {}

        def read():
            for line in self.p.stdout:
                line = line.strip()
                if not line.startswith('{'):
                    continue
                msg = json.loads(line)
                if msg.get('id') == body['id']:
                    result['msg'] = msg
                    return
        t = threading.Thread(target=read, daemon=True)
        t.start()
        t.join(self.timeout)
        if 'msg' not in result:
            raise RuntimeError('MCP server (stdio) did not answer — it may be waiting for a browser login')
        return result['msg']

    def close(self):
        if self.p.poll() is None:
            self.p.terminate()


def connect(spec):
    """http(s) URL -> HttpMCP; anything else is a server command -> StdioMCP."""
    return HttpMCP(spec) if spec.startswith(('http://', 'https://')) else StdioMCP(spec)


def reachable(url, timeout=3):
    try:
        urllib.request.urlopen(url.rsplit('/mcp', 1)[0] + '/', timeout=timeout).read(1)
        return True
    except urllib.error.HTTPError:
        return True
    except Exception:
        return False


if __name__ == '__main__':
    m = connect(sys.argv[2])
    if sys.argv[1] == 'list':
        for t in m.tools():
            if len(sys.argv) == 3 or any(k.lower() in t['name'].lower() for k in sys.argv[3:]):
                print(t['name'], '|', t.get('description', '')[:100].replace('\n', ' '))
    elif sys.argv[1] == 'call':
        print(m.tool(sys.argv[3], json.loads(sys.argv[4]))[:4000])
