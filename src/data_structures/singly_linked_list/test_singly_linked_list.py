import pytest
from singly_linked_list import Node, LinkedList


@pytest.fixture
def empty_list():
    """Returns an empty LinkedList instance."""
    return LinkedList()


@pytest.fixture
def single_element_list():
    """Returns a LinkedList with one element: [10]."""
    ll = LinkedList()

    ll.append(10)

    return ll


@pytest.fixture
def populated_list():
    """Returns a LinkedList: [10, 20, 30, 40]."""
    ll = LinkedList()

    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)

    return ll


def test_node_creation():
    node = Node(5)

    assert node.data == 5
    assert node.next is None


def test_node_repr():
    node = Node('test')

    assert repr(node) == "Node('test')"


def test_initial_state(empty_list):
    assert empty_list._head is None
    assert empty_list._tail is None
    assert len(empty_list) == 0
    assert empty_list.is_empty() is True
    assert str(empty_list) == "[]"
    assert repr(empty_list) == "LinkedList([])"


def test_len(populated_list):
    assert len(populated_list) == 4


def test_is_empty(empty_list, populated_list):
    assert empty_list.is_empty() is True
    assert populated_list.is_empty() is False


def test_to_list(populated_list):
    assert populated_list.to_list() == [10, 20, 30, 40]


def test_get_head_tail(populated_list):
    assert populated_list.get_head() == 10
    assert populated_list.get_tail() == 40


def test_get_head_tail_empty_raises_index_error(empty_list):
    with pytest.raises(IndexError):
        empty_list.get_head()

    with pytest.raises(IndexError):
        empty_list.get_tail()


def test_append_on_empty_list(empty_list):
    empty_list.append(1)

    assert empty_list._head.data == 1
    assert empty_list._tail.data == 1
    assert empty_list._head is empty_list._tail
    assert len(empty_list) == 1


def test_append_on_populated_list(populated_list):
    populated_list.append(50)

    assert populated_list._head.data == 10
    assert populated_list._tail.data == 50
    assert len(populated_list) == 5
    assert populated_list.to_list() == [10, 20, 30, 40, 50]


def test_prepend_on_empty_list(empty_list):
    empty_list.prepend(1)

    assert empty_list._head.data == 1
    assert empty_list._tail.data == 1
    assert empty_list._head is empty_list._tail
    assert len(empty_list) == 1


def test_prepend_on_populated_list(populated_list):
    populated_list.prepend(0)

    assert populated_list._head.data == 0
    assert populated_list._tail.data == 40
    assert len(populated_list) == 5
    assert populated_list.to_list() == [0, 10, 20, 30, 40]


def test_insert_at_start(populated_list):
    populated_list.insert(0, 5)

    assert populated_list.to_list() == [5, 10, 20, 30, 40]
    assert populated_list._head.data == 5
    assert len(populated_list) == 5


def test_insert_at_end(populated_list):
    populated_list.insert(4, 50)

    assert populated_list.to_list() == [10, 20, 30, 40, 50]
    assert populated_list._tail.data == 50
    assert len(populated_list) == 5


def test_insert_in_middle(populated_list):
    populated_list.insert(2, 25)

    assert populated_list.to_list() == [10, 20, 25, 30, 40]
    assert len(populated_list) == 5


def test_insert_out_of_range(populated_list):
    with pytest.raises(IndexError):
        populated_list.insert(-1, 99)

    with pytest.raises(IndexError):
        # Size is 4, max valid index for insert is 4
        populated_list.insert(5, 99)


def test_pop_left_single_element(single_element_list):
    data = single_element_list.pop_left()

    assert data == 10
    assert single_element_list.is_empty()
    assert single_element_list._head is None
    assert single_element_list._tail is None
    assert len(single_element_list) == 0


def test_pop_left_populated_list(populated_list):
    data = populated_list.pop_left()

    assert data == 10
    assert populated_list._head.data == 20
    assert populated_list._tail.data == 40
    assert len(populated_list) == 3
    assert populated_list.to_list() == [20, 30, 40]


def test_pop_left_empty_raises_index_error(empty_list):
    with pytest.raises(IndexError):
        empty_list.pop_left()


def test_pop_single_element(single_element_list):
    data = single_element_list.pop()

    assert data == 10
    assert single_element_list.is_empty()
    assert single_element_list._head is None
    assert single_element_list._tail is None
    assert len(single_element_list) == 0


def test_pop_populated_list(populated_list):
    data = populated_list.pop()

    assert data == 40
    assert populated_list._head.data == 10
    assert populated_list._tail.data == 30  # New tail is correct
    assert populated_list._tail.next is None  # Ensure old tail link is cut
    assert len(populated_list) == 3
    assert populated_list.to_list() == [10, 20, 30]


def test_pop_empty_raises_index_error(empty_list):
    with pytest.raises(IndexError):
        empty_list.pop()


def test_delete_head(populated_list):
    assert populated_list.delete(10) is True
    assert populated_list.to_list() == [20, 30, 40]
    assert populated_list._head.data == 20
    assert len(populated_list) == 3


def test_delete_tail(populated_list):
    assert populated_list.delete(40) is True
    assert populated_list.to_list() == [10, 20, 30]
    assert populated_list._tail.data == 30
    assert populated_list._tail.next is None
    assert len(populated_list) == 3


def test_delete_middle(populated_list):
    assert populated_list.delete(20) is True
    assert populated_list.to_list() == [10, 30, 40]
    assert len(populated_list) == 3


def test_delete_non_existent(populated_list):
    assert populated_list.delete(99) is False
    assert populated_list.to_list() == [10, 20, 30, 40]
    assert len(populated_list) == 4


def test_delete_single_element_list(single_element_list):
    assert single_element_list.delete(10) is True
    assert single_element_list.is_empty()
    assert len(single_element_list) == 0


def test_delete_empty_list(empty_list):
    assert empty_list.delete(10) is False


def test_delete_at_index_head(populated_list):
    data = populated_list.delete_at_index(0)

    assert data == 10
    assert populated_list.to_list() == [20, 30, 40]
    assert len(populated_list) == 3


def test_delete_at_index_tail(populated_list):
    data = populated_list.delete_at_index(3)

    assert data == 40
    assert populated_list.to_list() == [10, 20, 30]
    assert populated_list._tail.data == 30
    assert len(populated_list) == 3


def test_delete_at_index_middle(populated_list):
    data = populated_list.delete_at_index(1)

    assert data == 20
    assert populated_list.to_list() == [10, 30, 40]
    assert len(populated_list) == 3


def test_delete_at_index_out_of_range(populated_list):
    with pytest.raises(IndexError):
        populated_list.delete_at_index(-1)

    with pytest.raises(IndexError):
        populated_list.delete_at_index(4)


def test_find_data_exists(populated_list):
    assert populated_list.find(30) == 2
    assert populated_list.find(10) == 0
    assert populated_list.find(40) == 3


def test_find_data_not_exists(populated_list):
    assert populated_list.find(99) == -1


def test_find_empty_list(empty_list):
    assert empty_list.find(1) == -1


def test_get_valid_index(populated_list):
    assert populated_list.get(0) == 10
    assert populated_list.get(2) == 30
    assert populated_list.get(3) == 40


def test_get_out_of_range(populated_list):
    with pytest.raises(IndexError):
        populated_list.get(-1)

    with pytest.raises(IndexError):
        populated_list.get(4)


def test_reverse_populated_list(populated_list):
    populated_list.reverse()

    assert populated_list.to_list() == [40, 30, 20, 10]
    assert populated_list._head.data == 40
    assert populated_list._tail.data == 10


def test_reverse_single_element_list(single_element_list):
    single_element_list.reverse()

    assert single_element_list.to_list() == [10]
    assert single_element_list._head.data == 10
    assert single_element_list._tail.data == 10


def test_reverse_empty_list(empty_list):
    empty_list.reverse()

    assert empty_list.to_list() == []


def test_iterator(populated_list):
    result = []

    for data in populated_list:
        result.append(data)

    assert result == [10, 20, 30, 40]


def test_str_and_repr(populated_list):
    assert str(populated_list) == "[10, 20, 30, 40]"
    assert repr(populated_list) == "LinkedList([10, 20, 30, 40])"
