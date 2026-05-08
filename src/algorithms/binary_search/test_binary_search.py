import pytest
from binary_search import binary_search


def test_target_in_middle():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2


def test_target_at_start():
    assert binary_search([10, 20, 30, 40], 10) == 0


def test_target_at_end():
    assert binary_search([10, 20, 30, 40], 40) == 3


def test_target_not_present():
    assert binary_search([1, 3, 5, 7], 4) == -1
    assert binary_search([1, 3, 5, 7], 8) == -1
    assert binary_search([1, 3, 5, 7], 0) == -1


def test_empty_list():
    assert binary_search([], 5) == -1


def test_single_element_found():
    assert binary_search([10], 10) == 0


def test_single_element_not_found():
    assert binary_search([10], 5) == -1


def test_duplicate_elements():
    result = binary_search([1, 2, 2, 2, 3], 2)
    assert result in [1, 2, 3]


@pytest.mark.parametrize("arr, target, expected", [
    ([2, 4, 6, 8, 10], 6, 2),
    ([2, 4, 6, 8, 10], 2, 0),
    ([2, 4, 6, 8, 10], 10, 4),
    ([2, 4, 6, 8, 10], 5, -1),
])
def test_parametrized_cases(arr, target, expected):
    """Clean way to test multiple scenarios in one function."""
    assert binary_search(arr, target) == expected
