#!/usr/bin/env bash
# 生成覆盖率 HTML 报告
set -euo pipefail

pytest --cov=src/data_toolbox --cov-report=html
echo ""
echo "✅ 报告已生成: htmlcov/index.html"
