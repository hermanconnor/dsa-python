import pytest
from binary_search_recursive import binary_search_recursive


def test_recursive_find_middle():
    assert binary_search_recursive([1, 3, 5, 7, 9], 5) == 2


def test_recursive_find_first():
    assert binary_search_recursive([1, 3, 5, 7, 9], 1) == 0


def test_recursive_find_last():
    assert binary_search_recursive([1, 3, 5, 7, 9], 9) == 4


def test_recursive_not_found():
    assert binary_search_recursive([1, 3, 5, 7, 9], 4) == -1
    assert binary_search_recursive([1, 3, 5, 7, 9], 10) == -1


def test_recursive_explicit_bounds():
    """Verify that passing left and right manually works correctly."""
    nums = [10, 20, 30, 40, 50, 60]
    # Search for 20 only within the first half of the list
    assert binary_search_recursive(nums, 20, left=0, right=2) == 1
    # Search for 50 only within the second half
    assert binary_search_recursive(nums, 50, left=3, right=5) == 4
    # Attempt to find 10 when the bounds exclude it
    assert binary_search_recursive(nums, 10, left=2, right=5) == -1


def test_recursive_single_element():
    assert binary_search_recursive([100], 100) == 0
    assert binary_search_recursive([100], 200) == -1


def test_recursive_empty_list():
    assert binary_search_recursive([], 5) == -1


@pytest.mark.parametrize("arr, target, expected", [
    ([2, 4, 6, 8, 10, 12], 2, 0),
    ([2, 4, 6, 8, 10, 12], 12, 5),
    ([2, 4, 6, 8, 10, 12], 7, -1),
    ([1, 1, 1, 1], 1, 1),  # Should return the first 'mid' it hits
])
def test_recursive_scenarios(arr, target, expected):
    assert binary_search_recursive(arr, target) == expected
