# data-toolbox-cli

数据分析工具箱命令行工具，支持 **CSV / JSON** 文件的读取、清洗、统计分析与 Markdown 报告生成。

## 功能

| 命令 | 功能 |
|------|------|
| `data-toolbox start <文件>` | 查看数据概况（缺失值、样本数据） |
| `data-toolbox start <文件> -c <列名>` | 查看指定列的统计信息（均值/最值/中位数） |
| `data-toolbox clean <文件> -o <输出>` | 清洗数据：删除含缺失值的行 |
| `data-toolbox report <文件>` | 生成 Markdown 格式分析报告 |

## 安装

```bash
pip install -e .
```

或直接运行：

```bash
PYTHONPATH=src python -m data_toolbox.cli
```

## 使用示例

```bash
# 查看数据概况
data-toolbox start sales.csv

# 查看 "revenue" 列的统计
data-toolbox start sales.csv -c revenue

# 清洗并保存
data-toolbox clean sales.csv -o cleaned.csv

# 生成报告
data-toolbox report sales.csv > report.md
```

## 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 代码检查
ruff check .
```

## 项目结构

```
src/data_toolbox/      # 源码
├── analyzer.py        # 数据加载、清洗、统计
├── cli.py             # 命令行入口
└── reporter.py        # Markdown 报告生成

tests/                 # 测试
├── fixtures/          # 测试数据
└── test_*.py          # 单元测试
```

## 许可

MIT
