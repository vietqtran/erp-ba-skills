#!/usr/bin/env bash
# bpmn-kit — một lệnh cho cả chuỗi.
#   build.sh --init <thư-mục-dự-án>        tạo khung: defs/_common.py (danh mục) từ templates/
#   build.sh <thư-mục-dự-án> [BP-xx ...]   sinh bpmn/ docs/ viewer.html CAU-HOI-KHAO-SAT.md → render svg/ png/ → bpmnlint
# Dừng ở bước đầu tiên còn lỗi/cảnh báo; sửa defs/ rồi chạy lại.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

if [ "${1:-}" = "--init" ]; then
  P="${2:?thiếu thư mục dự án}"
  mkdir -p "$P/defs"
  [ -e "$P/defs/_common.py" ] || cp "$KIT/templates/_common.py" "$P/defs/_common.py"
  echo "Đã tạo $P/defs/_common.py — sửa danh mục, rồi viết defs/bpNN_*.py theo bpmn-kit/templates/vi_du_bp05.py (cú pháp: bpmn-kit/README.md)"
  exit 0
fi

P="$(cd "${1:?thiếu thư mục dự án}" && pwd)"; shift
[ -d "$KIT/node_modules" ] || (cd "$KIT" && PUPPETEER_SKIP_DOWNLOAD=1 npm install --no-fund --no-audit >/dev/null)
python3 "$KIT/scripts/bpmn_gen.py" "$P" "$@"
node "$KIT/scripts/render.mjs" "$P" "$@"
"$KIT/node_modules/.bin/bpmnlint" -c "$KIT/.bpmnlintrc" "$P"/bpmn/*.bpmn
echo "OK — $P: sinh, render, bpmnlint đều sạch"
