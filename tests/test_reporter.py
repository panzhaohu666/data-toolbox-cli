"""reporter 模块单元测试"""

from data_toolbox.analyzer import DataAnalyzer
from data_toolbox.reporter import generate_markdown


def test_generate_markdown_basic(sample_csv):
    """测试基本报告生成"""
    analyzer = DataAnalyzer(sample_csv)
    report = generate_markdown(analyzer)
    assert "数据分析报告" in report
    assert "数据概况" in report
    assert "行数" in report or "5" in report


def test_generate_markdown_columns(sample_csv):
    """测试报告中包含列信息"""
    analyzer = DataAnalyzer(sample_csv)
    report = generate_markdown(analyzer)
    assert "name" in report
    assert "age" in report
    assert "score" in report


def test_generate_markdown_stats(sample_csv):
    """测试报告中包含统计信息"""
    analyzer = DataAnalyzer(sample_csv)
    report = generate_markdown(analyzer)
    assert "均值" in report
    assert "最小值" in report
    assert "最大值" in report
