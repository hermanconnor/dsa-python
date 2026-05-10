import pytest
from bubble_sort import bubble_sort


def test_empty_list():
    """Should return an empty list when input is empty."""
    assert bubble_sort([]) == []


def test_single_element():
    """Should return the same list when there is only one element."""
    assert bubble_sort([1]) == [1]


def test_already_sorted():
    """Should remain sorted and handle the O(n) optimization case."""
    arr = [1, 2, 3, 4, 5]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    """Should correctly sort a list that is in descending order."""
    arr = [5, 4, 3, 2, 1]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]


def test_unsorted_list():
    """Standard random distribution test."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = sorted(arr)
    assert bubble_sort(arr) == expected


def test_duplicates():
    """Should handle multiple occurrences of the same value."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert bubble_sort(arr) == [1, 2, 2, 3, 3, 4, 8]


def test_negative_numbers():
    """Should correctly sort a mix of positive and negative numbers."""
    arr = [-3, 10, 0, -1, 5]
    assert bubble_sort(arr) == [-3, -1, 0, 5, 10]


def test_in_place_modification():
    """Verify that the original list object is actually modified."""
    original_list = [3, 2, 1]
    returned_list = bubble_sort(original_list)
    assert returned_list is original_list
    assert original_list == [1, 2, 3]


@pytest.mark.parametrize("arr, expected", [
    ([3, 1, 2], [1, 2, 3]),              # Standard unsorted
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse sorted
    ([1, 2, 3], [1, 2, 3]),              # Already sorted
    ([1], [1]),                          # Single element
    ([], []),                            # Empty list
    ([2, 2, 1, 1], [1, 1, 2, 2]),        # Duplicates
    ([-1, -5, 0, 2], [-5, -1, 0, 2]),    # Negatives
])
def test_bubble_sort_scenarios(arr, expected):
    """Tests various array configurations using parametrization."""
    assert bubble_sort(arr) == expected
