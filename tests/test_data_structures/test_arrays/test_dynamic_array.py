import pytest
from src.data_structures.arrays.dynamic_array import DynamicArray


@pytest.fixture
def empty_array():
    return DynamicArray()


@pytest.fixture
def filled_array(empty_array):
    arr = empty_array

    for i in range(5):
        arr.append(i + 10)

    return arr


def test_initial_state(empty_array):
    """Tests the initial properties of a newly created array."""
    assert len(empty_array) == 0
    assert empty_array.capacity() == 1
    assert empty_array.is_empty() is True


def test_append_basic(empty_array):
    empty_array.append(1)
    empty_array.append(2)

    assert len(empty_array) == 2
    assert empty_array[0] == 1
    assert empty_array[1] == 2


def test_capacity_increase(empty_array):
    """Tests the doubling of capacity when size meets capacity."""
    empty_array.append(1)
    assert empty_array.capacity() == 1

    empty_array.append(2)
    assert empty_array.capacity() == 2

    empty_array.append(3)
    assert empty_array.capacity() == 4

    empty_array.append(4)
    empty_array.append(5)
    assert empty_array.capacity() == 8

    # Check data integrity after multiple resizes
    assert [empty_array[i] for i in range(len(empty_array))] == [1, 2, 3, 4, 5]


def test_getitem_access(filled_array):
    """Tests positive and negative indexing for retrieval."""
    assert filled_array[0] == 10
    assert filled_array[4] == 14
    assert filled_array[-1] == 14
    assert filled_array[-5] == 10


def test_getitem_index_error(empty_array):
    """Tests out-of-bounds access raises IndexError."""
    with pytest.raises(IndexError):
        _ = empty_array[0]

    empty_array.append(5)
    with pytest.raises(IndexError):
        _ = empty_array[1]
    with pytest.raises(IndexError):
        _ = empty_array[-2]


def test_setitem_modify(filled_array):
    """Tests setting a new value using index access."""
    filled_array[2] = 99
    filled_array[-1] = 100

    assert filled_array[2] == 99
    assert filled_array[4] == 100
    assert len(filled_array) == 5


def test_insert_middle(filled_array):
    filled_array.insert(2, 55)

    assert len(filled_array) == 6
    assert filled_array[2] == 55
    assert filled_array[3] == 12


def test_insert_start(filled_array):
    filled_array.insert(0, 0)

    assert filled_array[0] == 0
    assert filled_array[1] == 10


def test_insert_end_valid(filled_array):
    filled_array.insert(len(filled_array), 20)

    assert filled_array[-1] == 20
    assert len(filled_array) == 6


def test_insert_index_error(filled_array):
    """Tests that insert raises IndexError for indices > size or < 0."""
    with pytest.raises(IndexError):
        filled_array.insert(len(filled_array) + 1, 99)  # Too high

    with pytest.raises(IndexError):
        filled_array.insert(-1, 99)


def test_insert_with_capacity_increase(empty_array):
    """Tests that insert correctly triggers a resize."""
    empty_array.append(1)
    empty_array.append(2)
    empty_array.append(3)
    assert empty_array.capacity() == 4

    # Current state: [1, 2, 3] (size=3, capacity=4)
    empty_array.insert(1, 99)  # Insert 99 at index 1
    # State: [1, 99, 2, 3] (size=4, capacity=4)
    assert len(empty_array) == 4
    assert empty_array.capacity() == 4

    empty_array.insert(0, 0)  # Trigger resize
    # State: [0, 1, 99, 2, 3] (size=5, capacity=8)
    assert len(empty_array) == 5
    assert empty_array.capacity() == 8
    assert [empty_array[i]
            for i in range(len(empty_array))] == [0, 1, 99, 2, 3]


def test_delete_positive_index(filled_array):
    deleted = filled_array.delete(1)

    assert deleted == 11
    assert len(filled_array) == 4
    assert [filled_array[i] for i in range(4)] == [10, 12, 13, 14]


def test_delete_negative_index(filled_array):
    deleted = filled_array.delete(-1)

    assert deleted == 14
    assert len(filled_array) == 4
    assert [filled_array[i] for i in range(4)] == [10, 11, 12, 13]


def test_delete_index_error(empty_array):
    """Tests deletion on empty array and out-of-bounds indices."""
    with pytest.raises(IndexError):
        empty_array.delete(0)

    empty_array.append(1)
    with pytest.raises(IndexError):
        empty_array.delete(1)

    with pytest.raises(IndexError):
        empty_array.delete(-2)


def test_delete_first_element(filled_array):
    """Tests deleting the first element (index 0)."""
    deleted = filled_array.delete(0)

    assert deleted == 10
    assert filled_array[0] == 11
    assert len(filled_array) == 4


def test_delete_last_element(filled_array):
    """Tests deleting the last element (index len-1 or -1)."""
    deleted = filled_array.delete(4)

    assert deleted == 14
    assert filled_array[-1] == 13
    assert len(filled_array) == 4


def test_delete_first_element_negative_index(filled_array):
    """Tests deleting the first element using negative index -size."""
    deleted = filled_array.delete(-5)  # -5 is the first element

    assert deleted == 10
    assert filled_array[0] == 11
    assert len(filled_array) == 4


def test_capacity_shrink_logic(empty_array):
    """Tests that capacity is halved when size < capacity // 4, and stops when size reaches 0."""
    # 1. Fill to capacity 8
    for i in range(7):
        empty_array.append(i)
    assert empty_array.capacity() == 8

    # 2. Delete until size=2. Still capacity=8.
    for _ in range(5):
        empty_array.delete(0)
    assert len(empty_array) == 2
    assert empty_array.capacity() == 8

    # 3. Delete 1 more. size=1. 1 < 8//4 (2). Triggers shrink to 4.
    empty_array.delete(0)
    assert len(empty_array) == 1
    assert empty_array.capacity() == 4

    # 4. Delete 1 more. size=0. Condition (self._size > 0) is now FALSE. NO SHRINK OCCURS.
    empty_array.delete(0)  # []
    assert len(empty_array) == 0
    # FIX: The expected capacity should be 4, as the shrink condition is self._size > 0.
    assert empty_array.capacity() == 4


def test_pop_default(filled_array):
    """Tests pop() which defaults to index -1."""
    popped = filled_array.pop()  # Pops 14
    assert popped == 14
    assert len(filled_array) == 4


def test_pop_arbitrary_index(filled_array):
    """Tests pop(index)."""
    popped = filled_array.pop(2)  # Pops 12
    assert popped == 12
    assert len(filled_array) == 4
    assert filled_array[2] == 13


def test_pop_empty_error(empty_array):
    """Tests pop on an empty array."""
    with pytest.raises(IndexError, match="pop from empty array"):
        empty_array.pop()


def test_index_found(filled_array):
    """Tests finding the index of an element."""
    filled_array.append(10)  # [10, 11, 12, 13, 14, 10]
    assert filled_array.index(10) == 0  # Should return the first occurrence
    assert filled_array.index(12) == 2


def test_index_not_found(filled_array):
    """Tests ValueError when element is not found."""
    with pytest.raises(ValueError, match="100 not in array"):
        filled_array.index(100)


def test_remove_found(filled_array):
    """Tests removing the first occurrence of a value."""
    filled_array.append(12)  # [10, 11, 12, 13, 14, 12]
    filled_array.remove(12)  # Removes the first 12
    assert len(filled_array) == 5
    assert [filled_array[i] for i in range(5)] == [10, 11, 13, 14, 12]


def test_remove_not_found(filled_array):
    """Tests ValueError when element is not found."""
    with pytest.raises(ValueError, match="100 not in array"):
        filled_array.remove(100)


def test_clear(filled_array):
    """Tests clearing the array and resetting its state."""
    filled_array.clear()
    assert len(filled_array) == 0
    assert filled_array.is_empty() is True
    assert filled_array.capacity() == 1  # Capacity should reset to 1


def test_string_representation(empty_array):
    """Tests the __str__ and __repr__ magic methods."""
    assert str(empty_array) == "[]"
    assert repr(empty_array) == "DynamicArray([])"

    empty_array.append(10)
    empty_array.append('a')

    assert str(empty_array) == "[10, a]"
    assert repr(empty_array) == "DynamicArray([10, 'a'])"
