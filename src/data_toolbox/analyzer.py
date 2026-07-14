import csv
import json
from typing import Any, Dict, List


class DataAnalyzer:
    """数据分析器：读取文件，清洗文件，计算统计"""

    def __init__(self, fileopen: str):
        self.fileopen = fileopen
        self.data: List[Dict[str, Any]] = []
        self._load()

    def _load(self):
        """加载CSV或者JSON文件"""
        if self.fileopen.endswith(".csv"):
            with open(self.fileopen, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
        elif self.fileopen.endswith(".json"):
            with open(self.fileopen, encoding="utf-8") as f:
                reader = json.load(f)
                self.data = list(reader)
        else:
            raise ValueError(f"不支持的文件格式：{self.fileopen}")

    # 删除含缺失值的行（检查 '' 和 None）
    def clean(self, drop_np: bool = True):
        """清洗数据：删除含缺失之的行，转换数值类型"""
        if drop_np:
            self.data = [
                row for row in self.data if all(v != "" and v is not None for v in row.values())
            ]
        # 尝试将数值列转化为float
        import contextlib
        for row in self.data:
            for key, value in row.items():
                with contextlib.suppress(ValueError, TypeError):
                    row[key] = float(value)

    # 返回某列的均值、最大值、最小值（自动转换类型）
    def stats(self, column: str) -> dict:
        """返回指定列的统计信息"""
        values = []
        for row in self.data:
            val = row.get(column)
            if val is not None and val != "":
                try:
                    if (num := float(val)) is not None:
                        values.append(num)
                except (ValueError, TypeError):
                    pass
        if not values:
            raise ValueError(f"列{column} 没有可用的数值数据")
        values.sort()
        n = len(values)
        return {
            "column": column,
            "count": n,
            "mean": sum(values) / n,
            "min": values[0],
            "max": values[-1],
            "median": values[n // 2] if n % 2 == 1 else (values[n // 2 - 1] + values[n // 2]) / 2,
        }

    # 返回每列的缺失值数量和数据概况
    def summary(self):
        """返回所有列的数据概括（缺失的数量，数据类型）"""
        if not self.data:
            return {}
        columns = self.data[0].keys()
        result = {}
        for col in columns:
            total = len(self.data)
            missing = sum(1 for row in self.data if row[col] in ("", None))

            sample_values = [row[col] for row in self.data[:3] if row[col] not in ("", None)]
            result[col] = {
                "total": total,
                "missing": missing,
                "missing_pct": f"{missing / total * 100:.1f}%",
                "sample_values": sample_values,
            }
        return result

    def save(self, out_path: str):
        """保存清洗后的数据到csv"""
        if not self.data:
            raise ValueError("没有数据可以保存")
        keys = self.data[0].keys()
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, keys)
            writer.writeheader()
            writer.writerows(self.data)
