# API 参考

## DataAnalyzer

```python
from data_toolbox.analyzer import DataAnalyzer
```

数据分析核心类，负责数据加载、清洗和统计计算。

### `__init__(self, fileopen: str)`

加载 CSV 或 JSON 文件。

| 参数 | 类型 | 说明 |
|------|------|------|
| `fileopen` | `str` | 文件路径，支持 `.csv` / `.json` |

**异常**: `ValueError` — 不支持的文件格式

---

### `clean(drop_na: bool = True)`

清洗数据：删除含缺失值的行，尝试将数值列转换为 `float`。

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `drop_na` | `bool` | `True` | 是否删除含缺失值的行 |

---

### `stats(column: str) -> dict`

返回指定列的统计信息。

**返回**:
```python
{
    "column": str,    # 列名
    "count": int,     # 有效数值数
    "mean": float,    # 均值
    "min": float,     # 最小值
    "max": float,     # 最大值
    "median": float,  # 中位数
}
```

**异常**: `ValueError` — 该列无可用数值数据

---

### `summary() -> dict`

返回所有列的数据概况。

**返回**:
```python
{
    "列名": {
        "total": int,        # 总行数
        "missing": int,      # 缺失值数量
        "missing_pct": str,  # 缺失百分比
        "sample_values": list,  # 前 3 个有效样本
    }
}
```

---

### `save(out_path: str)`

保存清洗后的数据为 CSV。

---

## generate_markdown

```python
from data_toolbox.reporter import generate_markdown
```

生成 Markdown 格式的数据分析报告。

```python
def generate_markdown(analyzer: DataAnalyzer) -> str:
    """传入已加载数据的 DataAnalyzer 实例，返回 Markdown 字符串"""
```

**示例**:
```python
analyzer = DataAnalyzer("data.csv")
md = generate_markdown(analyzer)
with open("report.md", "w") as f:
    f.write(md)
```
