# Python 项目完整骨架指南

> 本文档以 `data-toolbox-cli` 为实例，逐文件讲解一个标准 Python 项目的完整构成。
> 理解本文后，你将能够从零搭建、维护和发布一个规范的 Python 开源项目。

---

## 项目源码总览

打开仓库，你会看到以下文件。每个文件都有它存在的理由：

```
data-toolbox-cli/
│
├── pyproject.toml                 # ★ 项目的心脏：元信息、构建、工具配置都在这
├── README.md                      # ★ 门面：别人打开 GitHub 第一眼看到的东西
├── LICENSE                        # 许可证（没有它别人不敢用）
├── CHANGELOG.md                   # 版本变更记录
├── SECURITY.md                    # 安全漏洞报告流程
├── CODE_OF_CONDUCT.md             # 社区行为准则
├── CONTRIBUTING.md                # 贡献指南（告诉别人怎么参与开发）
│
├── src/                           # ★ 源码目录（推荐 src 布局）
│   └── data_toolbox/              # Python 包（就是一个目录 + __init__.py）
│       ├── __init__.py            # 包的入口，决定 `import data_toolbox` 能导入什么
│       ├── __about__.py           # 版本等元信息的唯一数据源
│       ├── analyzer.py            # 核心逻辑：数据加载、清洗、统计
│       ├── cli.py                 # 命令行入口（argparse）
│       ├── reporter.py            # 输出模块：生成 Markdown 报告
│       └── py.typed               # 告诉 mypy "我是个类型完备的包"
│
├── tests/                         # ★ 测试目录
│   ├── __init__.py                # 让 tests 成为一个包
│   ├── conftest.py                # 共享的测试夹具（fixtures）
│   ├── test_analyzer.py           # analyzer 模块的单元测试
│   ├── test_cli.py                # CLI 命令行集成测试
│   ├── test_reporter.py           # reporter 模块的单元测试
│   └── fixtures/                  # 测试数据
│       └── sample_data.csv
│
├── docs/                          # 文档
│   ├── usage.md                   # 使用指南
│   ├── api.md                     # API 参考
│   └── PROJECT_GUIDE.md           # ← 本文
│
├── .github/workflows/             # ★ CI/CD 自动化
│   ├── test.yml                   # 每次 push 自动跑测试
│   ├── publish.yml                # 打 tag 时自动发布到 PyPI
│   └── docs.yml                   # 文档自动部署到 GitHub Pages
│
├── scripts/                       # 开发辅助脚本
│   ├── setup-dev.sh               # 一键搭建开发环境
│   ├── quality-gate.sh            # 发布前质量门禁
│   └── coverage.sh                # 生成覆盖率 HTML 报告
│
├── Dockerfile                     # 容器化配置
├── .dockerignore                  # 构建镜像时忽略的文件
├── tox.ini                        # 多 Python 版本本地测试
├── Makefile                       # 常用命令快捷方式
├── .pre-commit-config.yaml        # git commit 前自动检查
├── .editorconfig                  # 跨编辑器统一缩进/编码
├── mkdocs.yml                     # 文档站点配置
├── .gitignore                     # Git 忽略规则
└── .env / .env.local              # 本地环境变量（不提交到 Git）
```

---

## 核心文件详解

### 1. `pyproject.toml` — 项目心脏

这是现代 Python 项目的唯一配置文件，替代了 `setup.py`、`setup.cfg`、`pytest.ini`、`.flake8` 等散落的配置。

```toml
[build-system]              # 告诉 pip 用什么工具构建
requires = ["hatchling"]    # hatchling 是目前最快的构建后端之一
build-backend = "hatchling.build"

[project]                   # 项目元信息（名称、版本、作者等）
name = "data-toolbox-cli"
dynamic = ["version"]       # 版本从 __about__.py 动态读取
requires-python = ">=3.8"

[project.optional-dependencies]   # 可选依赖分组
dev = ["pytest>=7", "ruff", "mypy"]  # pip install -e ".[dev]"
docs = ["mkdocs", "mkdocs-material"] # pip install -e ".[docs]"
test = ["pytest>=7", "tox"]         # pip install -e ".[test]"

[project.scripts]           # 安装后可以直接在终端运行
data-toolbox = "data_toolbox.cli:main"

[tool.mypy]                 # mypy 类型检查配置
strict = true               # 最严格的类型检查

[tool.ruff]                 # ruff 代码检查/格式化配置

[tool.pytest.ini_options]   # pytest 默认参数

[tool.coverage.run]         # 覆盖率统计配置
```

**为什么重要**：一个 `pip install -e .` 就能搞定一切，不用记各种命令。

---

### 2. `src/` 布局 — 为什么是 `src/`

传统的扁布局：
```
myproject/
├── mypackage/
│   └── __init__.py
├── tests/
└── setup.py
```

`src/` 布局：
```
myproject/
├── src/
│   └── mypackage/
│       └── __init__.py
├── tests/
└── pyproject.toml
```

**优势**：
- 强制你只能导入已安装的包（不能用相对路径乱导）
- 避免无意中导入项目根目录的同名目录
- 和测试环境完全隔离

---

### 3. `__init__.py` — 包的入口

```python
"""data-toolbox-cli — 数据分析工具箱命令行工具"""

from data_toolbox.__about__ import __version__, __author__, __license__
from data_toolbox.analyzer import DataAnalyzer
from data_toolbox.reporter import generate_markdown

__all__ = ["DataAnalyzer", "generate_markdown", "__version__", "__author__"]
```

**作用**：
- `__all__` 控制 `from data_toolbox import *` 能导入什么
- 从 `__about__.py` 集中管理版本号（DRY 原则）

---

### 4. `__about__.py` — 单一版本源

```python
__version__ = "0.1.0"
__author__ = "panzhaohu666"
__license__ = "MIT"
```

`pyproject.toml` 中通过 `dynamic = ["version"]` + `[tool.hatch.version] path = "src/data_toolbox/__about__.py"` 引用这里的版本。修改版本号只需要改这一个文件。

---

### 5. `py.typed` — 类型标记

一个**空文件**，告诉 mypy 和 IDE："我类型注解是完备的，放心做类型检查。"

没有它，`mypy` 会忽略你的包的类型信息。

---

### 6. GitHub Actions 三个 Workflow

#### `test.yml` — 持续集成
```yaml
on: [push, pull_request]         # 每次 push/PR 触发
strategy:
  matrix:
    python-version: ["3.9", "3.10", "3.11", "3.12"]  # 4 个版本并行跑
```

每次提交代码，GitHub 自动在 4 个 Python 版本上跑 lint + 测试。过了就是绿色勾，没过就报错。

#### `publish.yml` — 自动发布 PyPI
```yaml
on:
  push:
    tags: ["v*"]                 # 推送 v1.0.0 这样的 tag 时触发
```
打 tag 推送后，自动构建 wheel 并发布到 PyPI，`pip install data-toolbox-cli` 就能装。

#### `docs.yml` — 文档站点
`docs/` 目录内容变更时，自动用 mkdocs 生成 HTML 并部署到 GitHub Pages。

---

### 7. `conftest.py` — 测试装备库

```python
@pytest.fixture
def sample_csv(fixtures_dir: str) -> str:
    """返回示例 CSV 文件路径"""
    return os.path.join(fixtures_dir, "sample_data.csv")
```

所有测试文件都能直接用 `sample_csv` 参数拿到测试数据路径，不需要在每个文件重复写。

---

### 8. `tox.ini` — 本地多版本测试

CI 是在 GitHub 服务器上跑，`tox` 是在你本地模拟：

```ini
[tox]
envlist = py38, py39, py310, py311, py312, lint, mypy
```

`tox` 会为每个 Python 版本创建独立的虚拟环境，安装你的包，然后跑测试。推送前本地跑一遍 `tox`，避免 CI 失败。

---

### 9. `Dockerfile` — 容器化

```dockerfile
FROM python:3.12-slim AS builder   # 多阶段构建：先装包
FROM python:3.12-slim              # 再复制到干净镜像
ENTRYPOINT ["data-toolbox"]        # 默认命令
```

使用：
```bash
docker build -t data-toolbox .
docker run --rm -v $(pwd):/data data-toolbox start sample.csv
```

---

## 工具链全景

| 工具 | 用途 | 命令 |
|------|------|------|
| **hatchling** | 构建/打包 | `python -m build` |
| **pytest** | 测试 | `pytest -v` |
| **pytest-cov** | 覆盖率 | `pytest --cov` |
| **ruff** | 代码检查 + 格式化 | `ruff check . && ruff format .` |
| **mypy** | 类型检查 | `mypy src/data_toolbox` |
| **tox** | 多版本测试 | `tox` |
| **pre-commit** | git commit 钩子 | `pre-commit install` |
| **mkdocs** | 文档站点 | `mkdocs build` / `mkdocs serve` |

---

## 从零到发布的流程

### 开发阶段
```bash
git clone <repo> && cd <repo>
pip install -e ".[dev]"
pre-commit install          # 每次 commit 前自动 lint
# ... 写代码 ...
make test                   # 跑测试
make mypy                   # 类型检查
make lint                   # 代码风格
```

### 发布阶段
```bash
make quality                # 完整门禁（lint + mypy + test）
tox                         # 本地多版本验证
git tag v0.2.0              # 打版本 tag
git push --tags             # 推送，触发 CI 自动发布到 PyPI
```

### 质量门禁（quality gate）
```
ruff check     → 代码风格检查
ruff format    → 格式化检查
mypy           → 类型检查（strict 模式）
pytest         → 单元 + 集成测试（含覆盖率）
tox            → 多 Python 版本验证
```

所有门禁通过，才能发布。

---

## 常见问题

### Q: 为什么用 hatchling 而不是 setuptools？
hatchling 更快、配置更简洁、原生支持 `src/` 布局和 `dynamic version`。

### Q: 为什么用 ruff 而不是 flake8 + black + isort？
ruff 用 Rust 写成，速度是 flake8 的 100 倍，且一个工具同时做检查 + 格式化。

### Q: `py.typed` 真的需要吗？
如果没有它，`mypy` 检查你的包时会跳过类型信息。加上它是个好习惯。

### Q: 我应该什么时候用 `tox`？
在推送代码前本地跑一次，特别是准备发布新版本时。日常开发用 `make test` 就够了。

---

## 项目状态记录

| 指标 | 数值 |
|------|------|
| Python 版本 | 3.8+ |
| 测试数量 | 13 |
| 测试覆盖率 | analyzer: 100%, cli: 集成测试, reporter: 单元测试 |
| CI 平台 | GitHub Actions (4 × Python 版本) |
| 包管理器 | pip + hatchling |
| 代码风格 | ruff (pycodestyle + pyflakes + isort + bugbear + pyupgrade) |
| 类型检查 | mypy --strict |
| 许可证 | MIT |
