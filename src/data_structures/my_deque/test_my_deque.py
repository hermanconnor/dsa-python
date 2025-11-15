import pytest
from deque import Deque


@pytest.fixture
def empty_deque():
    """Returns an empty Deque instance."""
    return Deque()


@pytest.fixture
def populated_deque() -> Deque[int]:
    """Return a deque pre-populated with sample integers."""
    dq = Deque[int]()

    dq.append(10)
    dq.append(20)
    dq.append(30)

    return dq


def test_is_empty_initially(empty_deque):
    assert empty_deque.is_empty()
    assert len(empty_deque) == 0


def test_addppendleft(empty_deque):
    empty_deque.appendleft(1)
    empty_deque.appendleft(2)

    assert list(empty_deque) == [2, 1]


def test_append(empty_deque):
    empty_deque.append(1)
    empty_deque.append(2)

    assert list(empty_deque) == [1, 2]


def test_len_increments(empty_deque):
    empty_deque.appendleft(5)
    empty_deque.append(10)

    assert len(empty_deque) == 2


def test_popleft(populated_deque):
    assert populated_deque.popleft() == 10
    assert list(populated_deque) == [20, 30]
    assert len(populated_deque) == 2


def test_pop(populated_deque):
    assert populated_deque.pop() == 30
    assert list(populated_deque) == [10, 20]
    assert len(populated_deque) == 2


def test_popleft_until_empty(empty_deque):
    empty_deque.appendleft(1)

    assert empty_deque.popleft() == 1
    assert empty_deque.is_empty()


def test_popping_from_empty_raises(empty_deque):
    with pytest.raises(IndexError):
        empty_deque.popleft()

    with pytest.raises(IndexError):
        empty_deque.pop()


def test_peek_front_and_rear(populated_deque):
    assert populated_deque.peek_front() == 10
    assert populated_deque.peek_rear() == 30


def test_peek_on_empty_raises(empty_deque):
    with pytest.raises(IndexError):
        empty_deque.peek_front()

    with pytest.raises(IndexError):
        empty_deque.peek_rear()


def test_clear(populated_deque):
    populated_deque.clear()

    assert populated_deque.is_empty()
    assert len(populated_deque) == 0


def test_iteration(populated_deque):
    assert list(populated_deque) == [10, 20, 30]


def test_reversed_iteration(populated_deque):
    assert list(reversed(populated_deque)) == [30, 20, 10]


def test_contains(populated_deque):
    assert 20 in populated_deque
    assert 99 not in populated_deque


def test_getitem_positive_index(populated_deque):
    assert populated_deque[0] == 10
    assert populated_deque[1] == 20
    assert populated_deque[2] == 30


def test_getitem_negative_index(populated_deque):
    assert populated_deque[-1] == 30
    assert populated_deque[-2] == 20
    assert populated_deque[-3] == 10


def test_getitem_out_of_range(populated_deque):
    with pytest.raises(IndexError):
        _ = populated_deque[5]

    with pytest.raises(IndexError):
        _ = populated_deque[-4]


def test_equality():
    dq1 = Deque[int]()
    dq2 = Deque[int]()

    dq1.append(1)
    dq2.append(1)

    assert dq1 == dq2
    dq2.append(2)
    assert dq1 != dq2


def test_str_and_repr(populated_deque):
    s = str(populated_deque)

    assert "Deque" in s
    assert "10" in s
    assert "30" in s
    # repr should match str
    assert repr(populated_deque) == s
