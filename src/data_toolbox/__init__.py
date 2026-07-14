"""data-toolbox-cli — 数据分析工具箱命令行工具"""

from data_toolbox.analyzer import DataAnalyzer
from data_toolbox.reporter import generate_markdown

__all__ = ["DataAnalyzer", "generate_markdown"]
__version__ = "0.1.0"
