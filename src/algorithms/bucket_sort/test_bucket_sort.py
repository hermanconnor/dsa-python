import pytest
from bucket_sort import bucket_sort


@pytest.mark.parametrize("arr, expected", [
    ([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68],
     [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]),  # Floats
    ([10, 5, 5, 10, 2], [2, 5, 5, 10, 10]),                       # Duplicates
    # Already sorted
    ([100, 200, 300], [100, 200, 300]),
    # All identical
    ([50, 50, 50], [50, 50, 50]),
    ([], []),                                                      # Empty
    # Single element
    ([42], [42]),
])
def test_bucket_sort_scenarios(arr, expected):
    """Verifies bucket sort handles floats, duplicates, and small arrays."""
    assert bucket_sort(arr) == expected
