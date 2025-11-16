import pytest
from stacks_queue import StacksQueue


class TestStacksQueueInitialization:
    """Test queue initialization."""

    def test_init_creates_empty_queue(self):
        """Test that initialization creates an empty queue."""
        queue = StacksQueue[int]()

        assert queue.is_empty()
        assert len(queue) == 0


class TestEnqueue:
    """Test enqueue operations."""

    def test_enqueue_single_item(self):
        """Test enqueueing a single item."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        assert not queue.is_empty()
        assert len(queue) == 1

    def test_enqueue_multiple_items(self):
        """Test enqueueing multiple items."""
        queue = StacksQueue[int]()

        for i in range(5):
            queue.enqueue(i)

        assert len(queue) == 5

    def test_enqueue_different_types(self):
        """Test enqueueing different data types."""
        # Test with strings
        str_queue = StacksQueue[str]()

        str_queue.enqueue("hello")
        str_queue.enqueue("world")

        assert len(str_queue) == 2

        # Test with floats
        float_queue = StacksQueue[float]()

        float_queue.enqueue(3.14)
        float_queue.enqueue(2.71)

        assert len(float_queue) == 2


class TestDequeue:
    """Test dequeue operations."""

    def test_dequeue_single_item(self):
        """Test dequeueing a single item."""
        queue = StacksQueue[int]()

        queue.enqueue(42)
        result = queue.dequeue()

        assert result == 42
        assert queue.is_empty()

    def test_dequeue_fifo_order(self):
        """Test that dequeue follows FIFO order."""
        queue = StacksQueue[int]()

        items = [1, 2, 3, 4, 5]
        for item in items:
            queue.enqueue(item)

        for expected in items:
            assert queue.dequeue() == expected
        assert queue.is_empty()

    def test_dequeue_from_empty_queue_raises_error(self):
        """Test that dequeueing from empty queue raises IndexError."""
        queue = StacksQueue[int]()

        with pytest.raises(IndexError, match="dequeue from empty queue"):
            queue.dequeue()

    def test_dequeue_after_emptying_raises_error(self):
        """Test that dequeueing after emptying raises IndexError."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        queue.dequeue()

        with pytest.raises(IndexError, match="dequeue from empty queue"):
            queue.dequeue()


class TestPeek:
    """Test peek operations."""

    def test_peek_single_item(self):
        """Test peeking at a single item."""
        queue = StacksQueue[int]()

        queue.enqueue(42)

        assert queue.peek() == 42
        assert len(queue) == 1  # Peek doesn't remove item

    def test_peek_multiple_items(self):
        """Test peeking returns the front item."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        assert queue.peek() == 1
        assert len(queue) == 3

    def test_peek_from_empty_queue_raises_error(self):
        """Test that peeking at empty queue raises IndexError."""
        queue = StacksQueue[int]()

        with pytest.raises(IndexError, match="peek from empty queue"):
            queue.peek()

    def test_peek_does_not_modify_queue(self):
        """Test that peek doesn't modify the queue."""
        queue = StacksQueue[int]()

        items = [1, 2, 3]
        for item in items:
            queue.enqueue(item)

        # Peek multiple times
        for _ in range(3):
            assert queue.peek() == 1

        assert len(queue) == 3


class TestMixedOperations:
    """Test mixed enqueue and dequeue operations."""

    def test_interleaved_enqueue_dequeue(self):
        """Test interleaved enqueue and dequeue operations."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        queue.enqueue(2)

        assert queue.dequeue() == 1

        queue.enqueue(3)

        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.is_empty()

    def test_enqueue_after_complete_dequeue(self):
        """Test enqueueing after completely emptying the queue."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        queue.dequeue()
        queue.enqueue(2)

        assert queue.peek() == 2
        assert len(queue) == 1

    def test_multiple_cycles(self):
        """Test multiple cycles of filling and emptying."""
        queue = StacksQueue[int]()

        for cycle in range(3):
            # Fill the queue
            for i in range(5):
                queue.enqueue(cycle * 10 + i)

            # Empty the queue
            for i in range(5):
                assert queue.dequeue() == cycle * 10 + i

            assert queue.is_empty()


class TestIsEmpty:
    """Test is_empty method."""

    def test_is_empty_on_new_queue(self):
        """Test is_empty returns True for new queue."""
        queue = StacksQueue[int]()

        assert queue.is_empty()

    def test_is_empty_after_enqueue(self):
        """Test is_empty returns False after enqueue."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        assert not queue.is_empty()

    def test_is_empty_after_dequeue_to_empty(self):
        """Test is_empty returns True after dequeueing all items."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        queue.dequeue()

        assert queue.is_empty()


class TestSize:
    """Test size and __len__ methods."""

    def test_size_empty_queue(self):
        """Test size of empty queue."""
        queue = StacksQueue[int]()

        assert len(queue) == 0

    def test_size_after_enqueues(self):
        """Test size increases with enqueues."""
        queue = StacksQueue[int]()

        for i in range(10):
            queue.enqueue(i)
            assert len(queue) == i + 1

    def test_size_after_dequeues(self):
        """Test size decreases with dequeues."""
        queue = StacksQueue[int]()

        for i in range(5):
            queue.enqueue(i)

        for i in range(5):
            assert len(queue) == 5 - i
            queue.dequeue()

        assert len(queue) == 0

    def test_size_with_mixed_operations(self):
        """Test size with mixed operations."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        queue.enqueue(2)

        assert len(queue) == 2
        queue.dequeue()
        assert len(queue) == 1
        queue.enqueue(3)
        assert len(queue) == 2


class TestStringRepresentation:
    """Test string representation methods."""

    def test_str_empty_queue(self):
        """Test __str__ for empty queue."""
        queue = StacksQueue[int]()

        assert str(queue) == "Queue([])"

    def test_str_with_items(self):
        """Test __str__ with items."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        assert str(queue) == "Queue([1, 2, 3])"

    def test_str_after_dequeue(self):
        """Test __str__ after dequeue operations."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()

        assert str(queue) == "Queue([2, 3])"

    def test_repr_empty_queue(self):
        """Test __repr__ for empty queue."""
        queue = StacksQueue[int]()

        repr_str = repr(queue)

        assert "StacksQueue" in repr_str
        assert "size=0" in repr_str

    def test_repr_with_items(self):
        """Test __repr__ with items."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        queue.enqueue(2)
        repr_str = repr(queue)

        assert "StacksQueue" in repr_str
        assert "size=2" in repr_str


class TestTransferMechanism:
    """Test the internal transfer mechanism between stacks."""

    def test_transfer_happens_on_first_dequeue(self):
        """Test that transfer happens on first dequeue."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # Before dequeue, items are in enqueue_stack
        assert len(queue._enqueue_stack) == 3
        assert len(queue._dequeue_stack) == 0

        # After dequeue, items transferred to dequeue_stack
        queue.dequeue()
        assert len(queue._enqueue_stack) == 0
        assert len(queue._dequeue_stack) == 2

    def test_transfer_only_when_dequeue_stack_empty(self):
        """Test transfer only happens when dequeue_stack is empty."""
        queue = StacksQueue[int]()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()  # Triggers transfer

        queue.enqueue(3)
        queue.enqueue(4)

        # New items in enqueue_stack, old items still in dequeue_stack
        assert len(queue._enqueue_stack) == 2
        assert len(queue._dequeue_stack) == 1

        # Dequeue from dequeue_stack first
        assert queue.dequeue() == 2
        assert len(queue._dequeue_stack) == 0

        # Now transfer happens
        assert queue.dequeue() == 3
        assert len(queue._enqueue_stack) == 0


class TestEdgeCases:
    """Test edge cases and stress scenarios."""

    def test_large_number_of_items(self):
        """Test with a large number of items."""
        queue = StacksQueue[int]()
        n = 1000

        for i in range(n):
            queue.enqueue(i)

        assert len(queue) == n

        for i in range(n):
            assert queue.dequeue() == i

        assert queue.is_empty()

    def test_none_as_value(self):
        """Test that None can be stored in the queue."""
        queue = StacksQueue[type(None)]()

        queue.enqueue(None)

        assert queue.peek() is None
        assert queue.dequeue() is None

    def test_complex_objects(self):
        """Test with complex objects."""
        queue = StacksQueue[dict]()

        obj1 = {"name": "Alice", "age": 30}
        obj2 = {"name": "Bob", "age": 25}

        queue.enqueue(obj1)
        queue.enqueue(obj2)

        assert queue.dequeue() == obj1
        assert queue.dequeue() == obj2
