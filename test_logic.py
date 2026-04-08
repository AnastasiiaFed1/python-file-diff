import pytest
from logic import FileHandler

@pytest.fixture
def handler():
    return FileHandler()

@pytest.mark.parametrize("set_a, set_b, expected_same, expected_diff", [
    ({"apple", "banana"}, {"banana", "cherry"}, {"banana"}, {"apple", "cherry"}),
    ({"a", "b"}, {"a", "b"}, {"a", "b"}, set()),
    ({"x"}, {"y"}, set(), {"x", "y"}),
    (set(), {"z"}, set(), {"z"}),
])

def test_compare_sets(handler, set_a, set_b, expected_same, expected_diff):
    same, diff = handler.compare_sets(set_a, set_b)
    assert same == expected_same
    assert diff == expected_diff