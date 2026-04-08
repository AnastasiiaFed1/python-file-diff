import pytest
from logic import FileHandler

@pytest.fixture
def handler():
    return FileHandler()

def test_compare_sets_basic(handler):
    same, diff = handler.compare_sets({"apple"}, {"apple", "banana"})
    assert same == {"apple"}
    assert diff == {"banana"}