// Render <dự án>/bpmn/*.bpmn thành svg/*.svg và png/*.png bằng bpmn-js trong Chrome headless.
// Đồng thời là bài kiểm tra import: bpmn-js báo cảnh báo khi XML/DI có tham chiếu sai.
//   node render.mjs <thư-mục-dự-án>                 # tất cả
//   node render.mjs <thư-mục-dự-án> BP-05 BP-07     # chỉ các file bắt đầu bằng mã này
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import puppeteer from 'puppeteer-core';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(process.argv[2] || '.');
const viewer = path.join(here, '../node_modules/bpmn-js/dist/bpmn-navigated-viewer.production.min.js');
// Chrome hoặc Edge có sẵn trên máy (macOS, Windows, Linux); đặt CHROME_PATH để chỉ định khác.
const chrome = [
  process.env.CHROME_PATH,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
  '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/microsoft-edge',
].find((p) => p && fs.existsSync(p));
if (!chrome) {
  console.error('Không tìm thấy Chrome/Edge. Cài Chrome hoặc đặt biến CHROME_PATH tới file chạy của trình duyệt.');
  process.exit(2);
}

const only = process.argv.slice(3);
const files = fs.readdirSync(path.join(root, 'bpmn'))
  .filter((f) => f.endsWith('.bpmn'))
  .filter((f) => !only.length || only.some((o) => f.startsWith(o)))
  .sort();

const browser = await puppeteer.launch({ executablePath: chrome, headless: true, args: ['--no-sandbox'] });
let failed = 0;
try {
  const page = await browser.newPage();
  for (const file of files) {
    const xml = fs.readFileSync(path.join(root, 'bpmn', file), 'utf8');
    await page.setContent('<!doctype html><html><body style="margin:0"><div id="c" style="width:1600px;height:900px"></div></body></html>');
    await page.addScriptTag({ path: viewer });
    const res = await page.evaluate(async (xml) => {
      const v = new window.BpmnJS({ container: '#c' });
      try {
        const { warnings } = await v.importXML(xml);
        const { svg } = await v.saveSVG();
        return { svg, warnings: warnings.map((w) => w.message) };
      } catch (e) {
        return { error: String(e && e.message || e), warnings: (e.warnings || []).map((w) => w.message) };
      }
    }, xml);
    const slug = file.replace(/\.bpmn$/, '');
    if (res.error) {
      failed++;
      console.log(`✗ ${file}: ${res.error}`);
      res.warnings.forEach((w) => console.log(`    ! ${w}`));
      continue;
    }
    fs.writeFileSync(path.join(root, 'svg', slug + '.svg'), res.svg);
    const m = res.svg.match(/width="([\d.]+)" height="([\d.]+)"/);
    const w = Math.ceil(Number(m[1])), h = Math.ceil(Number(m[2]));
    const shot = await browser.newPage();
    await shot.setViewport({ width: w, height: h, deviceScaleFactor: 1.5 });
    await shot.setContent(`<!doctype html><html><body style="margin:0;background:#fff">${res.svg}</body></html>`);
    await shot.screenshot({ path: path.join(root, 'png', slug + '.png'), clip: { x: 0, y: 0, width: w, height: h } });
    await shot.close();
    if (res.warnings.length) failed++;
    console.log(`${res.warnings.length ? '!' : '✓'} ${file} → svg/png (${w}×${h})`);
    res.warnings.forEach((x) => console.log(`    ! ${x}`));
  }
} finally {
  await browser.close();
}
process.exit(failed ? 1 : 0);
