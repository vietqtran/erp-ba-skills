# rsd-kit — business-reader RSD from one BPMN process, exported to Word, published to Google Docs and Confluence

Use after `bpmn-kit`. It takes one `BP-xx` process that has already been drawn and writes a requirement specification (RSD) for business
readers. The document is in Vietnamese. It then publishes the RSD.

- One-shot prompt: [`PROMPT.md`](PROMPT.md)
- Approved sample: [`examples/tour-operator/rsd/BP-13`](../examples/tour-operator/rsd/BP-13/)

## Requirements

- Python 3, Node.js ≥ 18, Chrome or Edge, and `pandoc` (macOS: `brew install pandoc`).
- Publishing to Google Docs and Confluence needs one of the connection methods below.
- Without any connection, the scripts still work: they print steps to upload the Word file by hand.

## Commands (run from the repo root; `<RSD>` = `<project>/rsd/BP-xx`)

```bash
rsd-kit/scripts/render-diagrams.sh <RSD>                # diagrams/*.mmd -> images/*.png (first run installs mermaid-cli)
python3 rsd-kit/scripts/check.py <RSD>                  # frame, codes, images, book citations, no technical leftovers; "OK" = pass
rsd-kit/scripts/export-docx.sh <RSD>                    # -> RSD-*.docx (embedded images, bordered tables)
python3 rsd-kit/scripts/connect.py                      # which publishing method this machine can use
python3 rsd-kit/scripts/publish-gdocs.py <RSD>          # import the .docx, share "anyone with the link can view" (--share off|commenter|writer)
python3 rsd-kit/scripts/publish-confluence.py <RSD> --space <key|id> [--parent <page id>] [--dry-run]
```

- **Connection method.** Both publish scripts accept `--via auto|api|mcp|manual`. The default `auto` tries api → mcp → manual.
- **`publish-confluence.py`:**
  - Updates the page if the space already has one with the same title; otherwise creates it.
  - Uploads the images as attachments.
  - Builds the page in the BA team frame (`references/confluence-format.md`), then reads it back to verify.
  - Writes `<RSD>/.confluence.json`.
- **`publish-gdocs.py`:** if `<RSD>/.gdocs.json` exists it only prints the existing link; add `--new` to create another copy.
- **Preview without publishing:** `python3 rsd-kit/scripts/confluence_page.py <RSD>/RSD-*.md [--dialect storage] > page.html`.

## Connections

Settings are per user and live outside the repo, in `~/.config/rsd-kit/config.json` (sample: `templates/config.example.json`).
Environment variables do the same and take precedence. Configure only the targets you use.

| Method | Google Docs | Confluence |
|---|---|---|
| **API** (no MCP) | 1. Google Cloud Console: create a project, enable **Google Drive API**, set up the OAuth consent screen, and create an OAuth client ID of type **Desktop app**.<br>2. Save the JSON as `~/.config/rsd-kit/google-oauth-client.json`.<br>3. Run `python3 rsd-kit/scripts/connect.py google-login` once (opens a browser; scope `drive.file` only touches files created by the kit). | Create an API token at https://id.atlassian.com/manage-profile/security/api-tokens, then set `ATLASSIAN_SITE`, `ATLASSIAN_EMAIL`, `ATLASSIAN_API_TOKEN` (or `confluence.site/email/api_token` in the config). Pages are written in storage format. |
| **MCP over HTTP** | `RSD_GOOGLE_MCP=<url>` pointing to a [workspace-mcp](https://github.com/taylorwilsdon/google_workspace_mcp) server with the `import_to_google_doc` tool | `RSD_CONFLUENCE_MCP=<url>` pointing to an Atlassian Rovo MCP |
| **MCP over stdio** (the script starts the server) | `RSD_GOOGLE_MCP="uvx workspace-mcp --single-user --tools drive docs"` (needs `GOOGLE_OAUTH_CLIENT_ID/SECRET` as described by workspace-mcp) | `RSD_CONFLUENCE_MCP="npx -y mcp-remote https://mcp.atlassian.com/v2/mcp"` (first run opens a browser for the Atlassian login) |
| **Manual** | Upload the `.docx` to Drive → Open with Google Docs → share | Confluence → Import → Word document. This loses the lozenges, expand blocks and table of contents of the team frame |

- **MCP Manager:** its gateway `http://127.0.0.1:7717/mcp` is tried automatically. For another gateway set `MCP_GATEWAY` (applies to both targets).
- **AI session with its own Atlassian/Google tools** (e.g. claude.ai connectors) that the scripts cannot reach: follow `references/publish-with-agent-tools.md`.

## Layout

| Path | Content |
|---|---|
| `../books/TOPICS.md` | Process type → ERP topics → book chapters to read (shared with bpmn-kit) |
| `templates/book-notes.md` | Notes from the book chapters and where the RSD applies them (required, not published) |
| `templates/rsd-template.md` | Document frame (Vietnamese): sections 1–11, column names, code scheme. Keep section titles and column names unchanged; the scripts rely on them |
| `templates/diagrams/` | Mermaid render config, role colour classes |
| `templates/word-reference.docx` | Word style reference |
| `templates/config.example.json` | Connection config sample |
| `references/writing-guide.md` | What goes where from the BPMN, writing rules for business readers, list of diagrams |
| `references/confluence-format.md` | The BA team's RSD frame on Confluence (reference pages), mapping, publishing pitfalls |
| `references/publish-with-agent-tools.md` | Publishing with the AI session's MCP tools when the scripts cannot connect |
| `scripts/` | `connect.py` (detect and connect: API / MCP HTTP / MCP stdio), `mcp.py` (MCP client), diagram rendering, check, Word export, Confluence page builder and publisher, Google Docs publisher |

Each RSD folder contains `RSD-BP-xx.md`, `book-notes.md`, `diagrams/*.mmd`, `images/*.png`, the exported `.docx`, and the publish state files
`.confluence.json` and `.gdocs.json`.

## Limitations

- **API method:** tested against a mocked network only, not with real accounts. Run `publish-confluence.py --dry-run` the first time.
- **Page deletion:** Rovo MCP cannot delete pages, so pages created by mistake must be deleted by hand in Confluence.
- **Visual check:** the rendered page cannot be inspected without a browser login. Open the link once and check it, especially the paired figures.
