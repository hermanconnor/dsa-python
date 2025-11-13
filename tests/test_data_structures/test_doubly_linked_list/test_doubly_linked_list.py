import pytest
from src.data_structures.doubly_linked_list.doubly_linked_list import DoublyNode, DoublyLinkedList


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
