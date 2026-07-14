.PHONY: help install test test-cov lint fmt mypy quality tox clean

help:  ## 显示帮助信息
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

install:  ## 安装项目和开发依赖
	pip install -e ".[dev]"

test:  ## 运行测试
	pytest -v

test-cov:  ## 运行测试 + 覆盖率报告
	pytest -v --cov=src/data_toolbox --cov-report=term-missing

lint:  ## 代码检查（ruff）
	ruff check .
	ruff format --check .

fmt:  ## 自动格式化
	ruff format .
	ruff check --fix .

mypy:  ## 类型检查
	mypy src/data_toolbox

quality: lint mypy test  ## 完整质量门禁（lint + mypy + test）

tox:  ## 多 Python 版本测试
	tox

clean:  ## 清理缓存
	rm -rf __pycache__ .pytest_cache .mypy_cache .tox htmlcov dist build *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
