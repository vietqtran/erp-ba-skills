// Render thử mọi khối ```mermaid trong các file .md bằng thư viện Mermaid thật (tùy chọn, bổ sung cho `ba.py lint`).
//
// Cài một lần (trong thư mục bất kỳ, ví dụ ~/.cache/erp-ba-mermaid):
//   npm init -y && PUPPETEER_SKIP_DOWNLOAD=true npm install @mermaid-js/mermaid-cli
// Chạy:
//   MERMAID_NODE_MODULES=~/.cache/erp-ba-mermaid/node_modules node scripts/mermaid_check.mjs <thư-mục-hoặc-file.md> [...]
// Biến môi trường:
//   MERMAID_NODE_MODULES  đường dẫn node_modules chứa mermaid và puppeteer-core (bắt buộc nếu không cài cạnh script)
//   CHROME_PATH           đường dẫn Chrome/Chromium (mặc định thử /usr/bin/google-chrome, /usr/bin/chromium, macOS Chrome)
// Mã thoát: 0 = mọi sơ đồ render được; 1 = có sơ đồ lỗi (in vị trí file:dòng và thông báo lỗi).
import fs from 'fs'
import path from 'path'
import { createRequire } from 'module'
import { pathToFileURL } from 'url'

const nm = process.env.MERMAID_NODE_MODULES || path.join(path.dirname(new URL(import.meta.url).pathname), 'node_modules')
const require = createRequire(path.join(nm, 'noop.js'))
let puppeteer
try { puppeteer = (await import(pathToFileURL(require.resolve('puppeteer-core')).href)).default }
catch { console.error(`Không tìm thấy puppeteer-core trong ${nm}. Xem hướng dẫn cài ở đầu file.`); process.exit(2) }
const mermaidJs = path.join(path.dirname(require.resolve('mermaid/package.json')), 'dist', 'mermaid.min.js')
const chrome = process.env.CHROME_PATH || ['/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium', '/usr/bin/chromium-browser',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'].find(p => fs.existsSync(p))
if (!chrome) { console.error('Không tìm thấy Chrome/Chromium — đặt biến CHROME_PATH.'); process.exit(2) }

const files = []
const walk = p => { const st = fs.statSync(p); if (st.isDirectory()) fs.readdirSync(p).forEach(f => walk(path.join(p, f))); else if (p.endsWith('.md')) files.push(p) }
process.argv.slice(2).forEach(walk)
const blocks = []
for (const f of files) {
  const txt = fs.readFileSync(f, 'utf8')
  const re = /^```mermaid[ \t]*\n([\s\S]*?)^```/gm
  let m
  while ((m = re.exec(txt))) {
    if (m[1].includes('{{')) continue // khối còn placeholder của template
    blocks.push({ file: f, line: txt.slice(0, m.index).split('\n').length, code: m[1] })
  }
}
const browser = await puppeteer.launch({ executablePath: chrome, args: ['--no-sandbox', '--disable-gpu'], headless: true })
const page = await browser.newPage()
await page.setContent('<html><body></body></html>')
await page.addScriptTag({ path: mermaidJs })
await page.evaluate(() => mermaid.initialize({ startOnLoad: false, securityLevel: 'strict' }))
let bad = 0
for (const [i, b] of blocks.entries()) {
  const err = await page.evaluate(async (code, i) => {
    try { await mermaid.render('m' + i, code); return null } catch (e) { return String((e && e.message) || e) }
  }, b.code, i)
  if (err) { bad++; console.log(`LỖI ${b.file}:${b.line}\n  ${err.split('\n').slice(0, 5).join('\n  ')}`) }
}
console.log(`${blocks.length} sơ đồ đã kiểm, ${bad} lỗi`)
await browser.close()
process.exit(bad ? 1 : 0)
