# data-toolbox-cli

数据分析工具箱 CLI，支持 CSV / JSON 文件的读取、清洗、统计分析与 Markdown 报告生成。

## 快速开始

```bash
pip install data-toolbox-cli
data-toolbox start data.csv
```

## 命令一览

| 命令 | 功能 |
|------|------|
| `data-toolbox start <文件>` | 查看数据概况 |
| `data-toolbox start <文件> -c <列>` | 查看指定列统计 |
| `data-toolbox clean <文件> -o <输出>` | 清洗数据 |
| `data-toolbox report <文件>` | 生成 Markdown 报告 |

## 了解更多

- [使用指南](usage.md)
- [API 参考](api.md)
- [项目骨架指南](PROJECT_GUIDE.md)
