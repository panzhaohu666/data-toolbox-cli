import pytest
from analyzer import DataAnalyzer


def test_load_csv():
    analyzer = DataAnalyzer('/home/pzh/数据文件夹/数据内容.csv')
    assert len(analyzer.data) == 5


def test_stats_colum():
    analyzer = DataAnalyzer('/home/pzh/数据文件夹/数据内容.csv')
    result = analyzer.stats('age')
    assert 'mean' in result
    assert 'max' in result


def test_clean_drop_na():
    analyzer = DataAnalyzer('/home/pzh/数据文件夹/数据内容.csv')
    analyzer.clean()
    # 缺失值行已被移除
    assert all(v != '' for row in analyzer.data for v in row.values())


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        DataAnalyzer('nonexistent.csv')


def test_unsupported_type():
    with pytest.raises(ValueError, match='不支持'):
        DataAnalyzer('data.txt')
