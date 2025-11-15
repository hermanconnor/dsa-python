import pytest
from circular_queue import CircularQueue


def test_init_valid_capacity():
    q = CircularQueue(5)

    assert q.capacity == 5
    assert q.size == 0
    assert q.front == 0
    assert q.queue == [None] * 5


def test_init_invalid_capacity():
    with pytest.raises(ValueError):
        CircularQueue(0)

    with pytest.raises(ValueError):
        CircularQueue(-3)


def test_is_empty_and_is_full():
    q = CircularQueue(3)

    assert q.is_empty()
    assert not q.is_full()

    q.enqueue(10)
    assert not q.is_empty()

    q.enqueue(20)
    q.enqueue(30)
    assert q.is_full()


def test_enqueue_and_peek():
    q = CircularQueue(3)

    q.enqueue("A")
    assert q.peek() == "A"

    q.enqueue("B")
    assert q.peek() == "A"


def test_enqueue_full_raises():
    q = CircularQueue(2)

    q.enqueue(1)
    q.enqueue(2)

    with pytest.raises(IndexError):
        q.enqueue(3)


def test_dequeue_basic():
    q = CircularQueue(3)

    q.enqueue("x")
    q.enqueue("y")

    assert q.dequeue() == "x"
    assert q.dequeue() == "y"
    assert q.is_empty()


def test_dequeue_empty_raises():
    q = CircularQueue(2)

    with pytest.raises(IndexError):
        q.dequeue()


def test_circular_wraparound():
    q = CircularQueue(3)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # remove two items
    assert q.dequeue() == 1
    assert q.dequeue() == 2

    # now front index is 2
    q.enqueue(4)
    q.enqueue(5)

    # The queue should now contain [3, 4, 5] in order
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == 5
    assert q.is_empty()


def test_len():
    q = CircularQueue(4)

    assert len(q) == 0

    q.enqueue(10)
    q.enqueue(20)
    assert len(q) == 2

    q.dequeue()
    assert len(q) == 1


def test_str_representation():
    q = CircularQueue(3)

    assert str(q) == "[]"

    q.enqueue("a")
    q.enqueue("b")
    assert str(q) == "[a <- b]"


def test_repr_format():
    q = CircularQueue(3)

    r = repr(q)

    assert "CircularQueue" in r
    assert "capacity=3" in r
    assert "size=0" in r
