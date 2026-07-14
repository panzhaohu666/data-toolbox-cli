#!/usr/bin/env bash
# 本地开发环境一键安装
set -euo pipefail

python -m pip install --upgrade pip
pip install -e ".[dev,docs,test]"
pre-commit install

echo ""
echo "✅ 环境安装完成！"
echo "   make lint   — 代码检查"
echo "   make test   — 运行测试"
echo "   make mypy   — 类型检查"
echo "   tox         — 多版本测试"
