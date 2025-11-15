import pytest
from my_queue import Queue


@pytest.fixture
def empty_queue():
    """Returns an empty Queue instance."""
    return Queue()


@pytest.fixture
def populated_queue():
    """Returns a Queue with three elements: 10, 20, 30."""
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    return q


def test_initial_state(empty_queue):
    """Test that a new queue is empty and has size 0."""
    assert empty_queue.is_empty() is True
    assert len(empty_queue) == 0
    assert empty_queue.front is None
    assert empty_queue.rear is None


def test_enqueue_on_empty_queue(empty_queue):
    """Test enqueueing the first element."""
    empty_queue.enqueue(5)

    assert empty_queue.is_empty() is False
    assert len(empty_queue) == 1
    assert empty_queue.front.data == 5
    assert empty_queue.rear.data == 5


def test_multiple_enqueue(populated_queue):
    """Test enqueueing multiple elements (FIFO order check is implicit in dequeue)."""
    assert len(populated_queue) == 3
    assert populated_queue.front.data == 10
    assert populated_queue.rear.data == 30

    populated_queue.enqueue(40)

    assert len(populated_queue) == 4
    assert populated_queue.rear.data == 40
    # Ensure front hasn't changed
    assert populated_queue.front.data == 10


def test_peek_on_populated_queue(populated_queue):
    """Test peeking returns the front element without removal."""
    size_before = len(populated_queue)
    front_data = populated_queue.peek()

    assert front_data == 10
    assert len(populated_queue) == size_before
    assert populated_queue.front.data == 10


def test_peek_on_empty_queue(empty_queue):
    """Test peek raises IndexError on an empty queue."""
    with pytest.raises(IndexError) as e:
        empty_queue.peek()

    assert "peek from empty queue" in str(e.value)


def test_dequeue_on_populated_queue(populated_queue):
    """Test normal dequeue operation and FIFO behavior."""
    assert len(populated_queue) == 3

    # Dequeue 10
    dequeued_data_1 = populated_queue.dequeue()

    assert dequeued_data_1 == 10
    assert len(populated_queue) == 2
    assert populated_queue.front.data == 20  # New front

    # Dequeue 20
    dequeued_data_2 = populated_queue.dequeue()

    assert dequeued_data_2 == 20
    assert len(populated_queue) == 1
    assert populated_queue.front.data == 30  # New front


def test_dequeue_to_empty(populated_queue):
    """Test dequeuing the last element correctly resets front and rear to None."""
    # Dequeue first two elements
    populated_queue.dequeue()
    populated_queue.dequeue()

    # Dequeue the last element (30)
    dequeued_data = populated_queue.dequeue()

    assert dequeued_data == 30
    assert len(populated_queue) == 0
    assert populated_queue.is_empty() is True
    assert populated_queue.front is None
    assert populated_queue.rear is None


def test_dequeue_on_empty_queue(empty_queue):
    """Test dequeue raises IndexError on an empty queue."""
    with pytest.raises(IndexError) as e:
        empty_queue.dequeue()

    assert "dequeue from empty queue" in str(e.value)


def test_str_method(populated_queue):
    """Test the string representation of a populated queue."""
    expected_str = "Queue: [10, 20, 30] (Front -> Rear)"
    assert str(populated_queue) == expected_str


def test_str_method_empty(empty_queue):
    """Test the string representation of an empty queue."""
    expected_str = "Queue: [] (Front -> Rear)"
    assert str(empty_queue) == expected_str


def test_repr_method(populated_queue):
    """Test the official string representation."""
    expected_repr = "Queue(size=3, front=10)"
    assert repr(populated_queue) == expected_repr


def test_repr_method_empty(empty_queue):
    """Test the official string representation of an empty queue."""
    expected_repr = "Queue(size=0, front=None)"
    assert repr(empty_queue) == expected_repr


def test_mixed_operations(empty_queue):
    """Test a sequence of enqueue, dequeue, peek, and len operations."""
    q = empty_queue

    q.enqueue('A')
    q.enqueue('B')
    assert q.peek() == 'A'
    assert len(q) == 2

    assert q.dequeue() == 'A'
    assert len(q) == 1

    q.enqueue('C')
    q.enqueue('D')
    assert q.peek() == 'B'
    assert len(q) == 3

    assert q.dequeue() == 'B'
    assert q.dequeue() == 'C'

    assert q.dequeue() == 'D'
    assert q.is_empty() is True
    assert len(q) == 0

    # Ensure it can be used again after becoming empty
    q.enqueue(100)
    assert q.peek() == 100
    assert len(q) == 1
