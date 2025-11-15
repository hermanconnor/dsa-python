import pytest
from doubly_linked_list import DoublyNode, DoublyLinkedList


@pytest.fixture
def empty_list():
    """Returns an empty DoublyLinkedList."""
    return DoublyLinkedList()


@pytest.fixture
def populated_list():
    """Returns a DoublyLinkedList with [1, 2, 3, 4]."""
    dll = DoublyLinkedList()

    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)

    return dll


def test_doubly_node_initialization():
    node = DoublyNode("test")

    assert node.data == "test"
    assert node.prev is None
    assert node.next is None


def test_append_on_empty_list(empty_list):
    empty_list.append(10)

    assert empty_list._size == 1
    assert empty_list.head.data == 10
    assert empty_list.tail.data == 10
    assert empty_list.head.prev is None
    assert empty_list.head.next is None


def test_append_on_populated_list(populated_list):
    populated_list.append(5)

    assert populated_list._size == 5
    assert populated_list.tail.data == 5
    assert populated_list.tail.prev.data == 4
    assert populated_list.head.data == 1
    assert list(populated_list) == [1, 2, 3, 4, 5]


def test_prepend_on_empty_list(empty_list):
    empty_list.prepend(100)

    assert empty_list._size == 1
    assert empty_list.head.data == 100
    assert empty_list.tail.data == 100


def test_prepend_on_populated_list(populated_list):
    populated_list.prepend(0)

    assert populated_list._size == 5
    assert populated_list.head.data == 0
    assert populated_list.head.next.data == 1
    assert populated_list.head.next.prev.data == 0
    assert list(populated_list) == [0, 1, 2, 3, 4]


def test_insert_at_start_index_0(populated_list):
    populated_list.insert(0, 99)

    assert list(populated_list) == [99, 1, 2, 3, 4]
    assert populated_list.head.data == 99
    assert populated_list.head.next.data == 1


def test_insert_at_end_index_size(populated_list):
    populated_list.insert(4, 99)

    assert list(populated_list) == [1, 2, 3, 4, 99]
    assert populated_list.tail.data == 99
    assert populated_list.tail.prev.data == 4


def test_insert_in_middle(populated_list):
    populated_list.insert(2, 99)

    assert list(populated_list) == [1, 2, 99, 3, 4]

    node_99 = populated_list._get_node(2)

    assert node_99.data == 99
    assert node_99.prev.data == 2
    assert node_99.next.data == 3
    assert populated_list._size == 5


def test_insert_index_out_of_range(populated_list):
    with pytest.raises(IndexError):
        populated_list.insert(5, 99)

    with pytest.raises(IndexError):
        populated_list.insert(-1, 99)


def test_delete_by_value_head(populated_list):
    assert populated_list.delete(1) is True

    assert list(populated_list) == [2, 3, 4]
    assert populated_list.head.data == 2
    assert populated_list.head.prev is None
    assert populated_list._size == 3


def test_delete_by_value_tail(populated_list):
    assert populated_list.delete(4) is True
    assert list(populated_list) == [1, 2, 3]
    assert populated_list.tail.data == 3
    assert populated_list.tail.next is None
    assert populated_list._size == 3


def test_delete_by_value_middle(populated_list):
    assert populated_list.delete(2) is True
    assert list(populated_list) == [1, 3, 4]

    node_1 = populated_list.head
    node_3 = node_1.next

    assert node_1.next.data == 3
    assert node_3.prev.data == 1
    assert populated_list._size == 3


def test_delete_by_value_not_found(populated_list):
    assert populated_list.delete(99) is False
    assert populated_list._size == 4


def test_delete_at_index_head(populated_list):
    deleted_data = populated_list.delete_at_index(0)

    assert deleted_data == 1
    assert list(populated_list) == [2, 3, 4]
    assert populated_list._size == 3


def test_delete_at_index_tail(populated_list):
    deleted_data = populated_list.delete_at_index(3)

    assert deleted_data == 4
    assert list(populated_list) == [1, 2, 3]
    assert populated_list._size == 3


def test_delete_at_index_invalid(populated_list):
    with pytest.raises(IndexError):
        populated_list.delete_at_index(4)


def test_clear(populated_list):
    populated_list.clear()

    assert populated_list.is_empty() is True
    assert populated_list.head is None
    assert populated_list.tail is None
    assert populated_list._size == 0


def test_reverse(populated_list):
    populated_list.reverse()

    assert list(populated_list) == [4, 3, 2, 1]
    assert populated_list.head.data == 4
    assert populated_list.tail.data == 1
    assert populated_list.head.next.data == 3
    assert populated_list.tail.prev.data == 2


def test_find_forward(populated_list):
    populated_list.append(2)  # [1, 2, 3, 4, 2]

    assert populated_list.find(2) == 1  # Finds first occurrence
    assert populated_list.find(4) == 3
    assert populated_list.find(99) == -1


def test_find_from_tail_backward(populated_list):
    populated_list.prepend(3)  # [3, 1, 2, 3, 4]
    # Finds last occurrence at index 3
    assert populated_list.find_from_tail(3) == 3
    assert populated_list.find_from_tail(1) == 1
    assert populated_list.find_from_tail(99) == -1


def test_get_head_tail(empty_list):
    with pytest.raises(IndexError):
        empty_list.get_head()

    with pytest.raises(IndexError):
        empty_list.get_tail()


def test_get_head_tail(populated_list):
    assert populated_list.get_head() == 1
    assert populated_list.get_tail() == 4


def test_len(populated_list, empty_list):
    assert len(populated_list) == 4
    assert len(empty_list) == 0


def test_iter(populated_list):
    data = [item for item in populated_list]
    assert data == [1, 2, 3, 4]


def test_contains(populated_list):
    # Test 'in' operator
    assert 3 in populated_list
    assert 99 not in populated_list


def test_getitem(populated_list):
    # Test list[index]
    assert populated_list[0] == 1
    assert populated_list[3] == 4

    with pytest.raises(IndexError):
        _ = populated_list[4]


def test_setitem(populated_list):
    # Test list[index] = data
    populated_list[1] = 99

    assert list(populated_list) == [1, 99, 3, 4]
    assert populated_list._get_node(1).data == 99


def test_delitem(populated_list):
    # Test del list[index]
    del populated_list[1]  # Delete 2

    assert list(populated_list) == [1, 3, 4]
    assert len(populated_list) == 3

    with pytest.raises(IndexError):
        del populated_list[3]


def test_repr_str(populated_list):
    # Test __repr__
    assert repr(populated_list) == "DoublyLinkedList([1, 2, 3, 4])"
    # Test __str__
    assert str(populated_list) == "[1, 2, 3, 4]"


def test_reversed(populated_list):
    # Test reverse iteration
    data = [item for item in reversed(populated_list)]
    assert data == [4, 3, 2, 1]
