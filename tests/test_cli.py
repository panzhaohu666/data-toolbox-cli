"""CLI 命令行集成测试"""

import subprocess
import sys
from pathlib import Path


def _cli(args: list[str]) -> subprocess.CompletedProcess:
    """运行 CLI 命令"""
    cmd = [sys.executable, "-m", "data_toolbox.cli"] + args
    return subprocess.run(cmd, capture_output=True, text=True, cwd=str(Path(__file__).parent))


def test_start_summary(sample_csv):
    """测试 start 命令 — 显示数据概况"""
    result = _cli(["start", sample_csv])
    assert result.returncode == 0
    assert "name" in result.stdout
    assert "age" in result.stdout
    assert "score" in result.stdout


def test_start_column_stats(sample_csv):
    """测试 start -c 命令 — 显示指定列统计"""
    result = _cli(["start", sample_csv, "-c", "age"])
    assert result.returncode == 0
    assert "mean" in result.stdout.lower() or "mean" in result.stdout


def test_clean(sample_csv, temp_output):
    """测试 clean 命令 — 清洗数据并保存"""
    result = _cli(["clean", sample_csv, "-o", temp_output])
    assert result.returncode == 0
    assert "清洗完成" in result.stdout
    assert Path(temp_output).exists()


def test_report(sample_csv):
    """测试 report 命令 — 生成分析报告"""
    result = _cli(["report", sample_csv])
    assert result.returncode == 0
    assert "数据分析报告" in result.stdout


def test_file_not_found():
    """测试文件不存在时的错误处理"""
    result = _cli(["start", "nonexistent.csv"])
    assert result.returncode != 0
    assert "不存在" in result.stdout or "错误" in result.stdout
