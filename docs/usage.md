# 使用指南

## 快速开始

```bash
# 安装
pip install -e .

# 查看帮助
data-toolbox --help
```

## 命令详解

### start — 查看数据

```bash
# 查看所有列的概况（缺失数、样本值）
data-toolbox start data.csv

# 查看指定列的统计信息
data-toolbox start data.csv -c age
```

### clean — 清洗数据

```bash
# 删除含缺失值的行，保存到新文件
data-toolbox clean data.csv -o cleaned.csv
```

### report — 生成报告

```bash
# 输出 Markdown 报告到终端
data-toolbox report data.csv

# 保存到文件
data-toolbox report data.csv > report.md
```

## 支持的数据格式

| 格式 | 说明 |
|------|------|
| `.csv` | 逗号分隔值，UTF-8 编码 |
| `.json` | JSON 对象数组 `[{...}, {...}]` |

## 报告内容

生成的 Markdown 报告包含：

1. **数据概况** — 行数、列数、来源文件
2. **各列概况** — 总数、缺失值、缺失率、样本值
3. **数值统计** — 均值、最值、中位数、有效数据量

## 示例数据

`tests/fixtures/sample_data.csv` 提供了一个含缺失值的示例数据集：

| name | age | score |
|------|-----|-------|
| Alice | 25 | 85.5 |
| Bob | 30 | 92.0 |
| Charlie | (缺失) | 78.3 |
| Diana | 28 | 88.7 |
| Eve | 35 | (缺失) |
