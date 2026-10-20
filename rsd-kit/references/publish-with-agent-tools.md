# Publishing with the AI session's own MCP tools

Use this when `connect.py` reports "manual" but the Claude Code session has Atlassian or Google tools (e.g. claude.ai connectors).
The scripts cannot call those tools, so the agent does the steps below itself.

A quicker alternative is to point the scripts at the same server, by URL or stdio command (README, section "Connections").

## Confluence (Atlassian Rovo MCP: createConfluenceContent, updateConfluenceContent, …)

1. Get the cloudId with `getAccessibleAtlassianResources`.
2. Find the space with `listConfluenceSpaces`. Read `getConfluenceSpace` and apply the space instructions, if any.
3. Look for a page with the same title with `listConfluenceContent` (type page, spaceId). **Never create a duplicate.**
4. Run `python3 rsd-kit/scripts/confluence_page.py <RSD>/RSD-*.md > /tmp/page.html`.
   - If the page does not exist yet, create it with that body (`createConfluenceContent`, format html).
   - If it already exists, note its page id.
5. For each `images/*.png`:
   1. Call `createConfluenceAttachment` (through executeWrite).
   2. Run the returned `uploadCommand`. Never print the token.
   3. Record the `fileId` in `/tmp/files.json` as `{"h01-….png": "<fileId>"}`.
6. Run `python3 rsd-kit/scripts/confluence_page.py <RSD>/RSD-*.md --files /tmp/files.json --page-id <id> > /tmp/page.html`.
7. Call `updateConfluenceContent` with the latest `snapshotToken`. **Do not send `title`.**
8. Read the page back with `getConfluenceContent` (detail full). Compare the counts of images, tables and expand blocks.

**Non-Rovo Atlassian servers** (e.g. mcp-atlassian, which accepts storage format): use `--dialect storage`. Images then reference
the attachment file name, so no fileId is needed.

## Google Docs

- **The server has a file-import tool** (e.g. `import_to_google_doc`): send the `.docx` as base64, then enable "anyone with the link can view".
- **The server can only create a Doc from text:** do not use it, because images and tables would be lost. Give the user the manual steps
  printed by `publish-gdocs.py` instead.
