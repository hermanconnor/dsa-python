import pytest
from bucket_sort_uniform import bucket_sort_uniform


@pytest.mark.parametrize("arr, expected", [
    ([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434],
     [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]),  # Standard Uniform
    ([0.0, 0.5, 1.0], [0.0, 0.5, 1.0]),             # Boundary values
    ([0.9, 0.1, 0.1, 0.9], [0.1, 0.1, 0.9, 0.9]),   # Duplicates
    ([0.2, 0.2, 0.2], [0.2, 0.2, 0.2]),             # All identical
    ([], []),                                       # Empty
    ([0.5], [0.5]),                                 # Single element
])
def test_bucket_sort_uniform_scenarios(arr, expected):
    """Tests the uniform bucket sort with range-specific floating point data."""
    assert bucket_sort_uniform(arr) == expected
