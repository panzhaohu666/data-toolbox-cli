import os

import pytest

from data_toolbox.analyzer import DataAnalyzer

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")
SAMPLE_CSV = os.path.join(FIXTURES, "sample_data.csv")


def test_load_csv():
    analyzer = DataAnalyzer(SAMPLE_CSV)
    assert len(analyzer.data) == 5


def test_stats_column():
    analyzer = DataAnalyzer(SAMPLE_CSV)
    result = analyzer.stats("age")
    assert "mean" in result
    assert "max" in result


def test_clean_drop_na():
    analyzer = DataAnalyzer(SAMPLE_CSV)
    analyzer.clean()
    # 缺失值行已被移除
    assert all(v != "" for row in analyzer.data for v in row.values())


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        DataAnalyzer("nonexistent.csv")


def test_unsupported_type():
    with pytest.raises(ValueError, match="不支持"):
        DataAnalyzer("data.txt")
