import os
import tempfile

import pytest


@pytest.fixture
def fixtures_dir() -> str:
    """返回测试数据目录"""
    return os.path.join(os.path.dirname(__file__), "fixtures")


@pytest.fixture
def sample_csv(fixtures_dir: str) -> str:
    """返回示例 CSV 文件路径"""
    return os.path.join(fixtures_dir, "sample_data.csv")


@pytest.fixture
def temp_output() -> str:
    """返回临时输出文件路径（测试结束后自动清理）"""
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
        pass
    yield f.name
    if os.path.exists(f.name):
        os.unlink(f.name)
