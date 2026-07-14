#!/usr/bin/env bash
# 发布前质量门禁
set -euo pipefail

echo "🔍 ruff check..."
ruff check .

echo "🔍 ruff format..."
ruff format --check .

echo "🔍 mypy..."
mypy src/data_toolbox

echo "🧪 pytest..."
pytest -v --cov=src/data_toolbox --cov-report=term-missing

echo ""
echo "✅ 质量门禁全部通过！"
