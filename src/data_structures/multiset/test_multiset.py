import ast
import pytest
from collections import Counter
from multiset import Multiset


@pytest.fixture
def empty_multiset():
    """Returns an empty Multiset instance."""
    return Multiset()


@pytest.fixture
def populated_multiset():
    """Returns a Multiset with 3 apples, 2 bananas, and 1 orange."""
    multiset = Multiset()

    multiset.add("apple")
    multiset.add("banana")
    multiset.add("apple")
    multiset.add("orange")
    multiset.add("banana")
    multiset.add("apple")

    return multiset


def test_initialization(empty_multiset):
    """Tests that a new bag is empty and has a size of zero."""
    assert empty_multiset.is_empty() is True
    assert len(empty_multiset) == 0
    assert empty_multiset.items == Counter()


def test_initialization_with_iterable():
    """Tests initializing the Multiset with a list of items."""
    items = ["apple", "banana", "apple", "orange", "banana", "apple"]
    multiset = Multiset(items)

    assert len(multiset) == 6
    assert multiset.is_empty() is False
    assert multiset.count("apple") == 3
    assert multiset.count("banana") == 2
    assert multiset.count("orange") == 1
    assert "grape" not in multiset


def test_initialization_with_other_iterables():
    """Tests initializing the Multiset with other iterable types like tuples and strings."""
    # Test with a tuple
    tuple_multiset = Multiset(("a", "b", "a"))
    assert len(tuple_multiset) == 3
    assert tuple_multiset.count("a") == 2

    # Test with a string (iterates through characters)
    string_multiset = Multiset("mississippi")
    assert len(string_multiset) == 11
    assert string_multiset.count("i") == 4
    assert string_multiset.count("s") == 4
    assert string_multiset.count("p") == 2
    assert string_multiset.count("m") == 1


def test_updated_contains_method(empty_multiset):
    """
    Tests that checking containment on missing items works
    without inserting keys into the underlying Counter.
    """
    assert "missing_key" not in empty_multiset

    # Ensure that checking containment did not create the key in the counter
    assert "missing_key" not in empty_multiset.items
    assert len(empty_multiset.items) == 0


def test_add_single_item(empty_multiset):
    """Tests adding a single item."""
    empty_multiset.add("mango")

    assert len(empty_multiset) == 1
    assert empty_multiset.count("mango") == 1
    assert empty_multiset.items == Counter({"mango": 1})


def test_add_multiple_items(populated_multiset):
    """Tests adding multiple items and checking counts."""
    assert len(populated_multiset) == 6
    assert populated_multiset.count("apple") == 3
    assert populated_multiset.count("banana") == 2
    assert populated_multiset.count("orange") == 1
    assert populated_multiset.count("grape") == 0


def test_contains_method(populated_multiset):
    """Tests the __contains__ ('in') operator."""
    assert "apple" in populated_multiset
    assert "banana" in populated_multiset
    assert "orange" in populated_multiset
    assert "grape" not in populated_multiset
    assert populated_multiset.count("grape") == 0


def test_remove_single_occurrence(populated_multiset):
    """Tests removing an item that has multiple occurrences."""
    initial_len = len(populated_multiset)
    initial_apple_count = populated_multiset.count("apple")

    assert populated_multiset.remove("apple") is True
    assert len(populated_multiset) == initial_len - 1
    assert populated_multiset.count("apple") == initial_apple_count - 1
    # Ensure the item is still in the internal Counter since count is > 0
    assert "apple" in populated_multiset.items


def test_remove_last_occurrence(populated_multiset):
    """Tests removing an item's last occurrence, ensuring cleanup."""
    assert populated_multiset.remove("orange") is True
    assert populated_multiset.count("orange") == 0
    assert "orange" not in populated_multiset
    # Check that the key was removed from the internal Counter
    assert "orange" not in populated_multiset.items
    assert len(populated_multiset) == 5


def test_remove_nonexistent_item(populated_multiset):
    """Tests attempting to remove an item not in the bag."""
    initial_len = len(populated_multiset)

    assert populated_multiset.remove("kiwi") is False
    assert len(populated_multiset) == initial_len
    assert populated_multiset.remove("mango") is False
    assert len(populated_multiset) == initial_len


def test_iteration(populated_multiset):
    """Tests that __iter__ yields all elements, including duplicates."""
    # The elements should be yielded in the order they were first added
    expected_order = ["apple", "apple", "apple", "banana", "banana", "orange"]

    # We use sorted to ensure the test passes regardless of the insertion order,
    # as Counter.elements() is guaranteed to return items grouped by element,
    # but the order of the groups might vary based on Python version/implementation.
    assert sorted(list(populated_multiset)) == sorted(expected_order)
    assert len(list(populated_multiset)) == 6


def test_repr_method(populated_multiset):
    """Tests the string representation."""
    expected_repr = "Multiset({'apple': 3, 'banana': 2, 'orange': 1})"

    assert repr(populated_multiset) == expected_repr


def test_updated_repr_method(populated_multiset):
    """Tests the new __repr__ output matching the Multiset class name."""
    # 1. Capture the actual __repr__ string
    actual_repr = repr(populated_multiset)

    # 2. Verify it starts and ends correctly
    assert actual_repr.startswith("Multiset({")
    assert actual_repr.endswith("})")

    # 3. Extract the inner dictionary string and parse it safely
    # This strips away 'Multiset(' and ')' to leave just the dictionary string
    dict_part = actual_repr[9:-1]

    # ast.literal_eval converts the string "{'apple': 3, ...}" back into a Python dict
    parsed_dict = ast.literal_eval(dict_part)

    # 4. Assert the contents match exactly
    assert parsed_dict == {"apple": 3, "banana": 2, "orange": 1}


def test_removal_until_empty(populated_multiset):
    """Tests removing all items until the multiset is empty."""
    populated_multiset.remove("apple")
    populated_multiset.remove("apple")
    populated_multiset.remove("apple")
    populated_multiset.remove("banana")
    populated_multiset.remove("banana")
    populated_multiset.remove("orange")

    assert len(populated_multiset) == 0
    assert populated_multiset.is_empty() is True
    assert "apple" not in populated_multiset.items
    assert "banana" not in populated_multiset.items
    assert "orange" not in populated_multiset.items
