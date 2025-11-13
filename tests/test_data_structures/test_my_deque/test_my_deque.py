import pytest
from src.data_structures.my_deque.deque import Node, Deque


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
