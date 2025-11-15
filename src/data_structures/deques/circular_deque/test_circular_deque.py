import pytest
from circular_deque import CircularDeque


class TestCircularDequeInitialization:
    """Test deque initialization and basic properties."""

    def test_default_initialization(self):
        """Test creating a deque with default capacity."""
        deque = CircularDeque()

        assert len(deque) == 0
        assert deque.is_empty()
        assert deque._capacity == CircularDeque.MIN_CAPACITY

    def test_custom_capacity(self):
        """Test creating a deque with custom capacity."""
        deque = CircularDeque(capacity=16)

        assert len(deque) == 0
        assert deque._capacity == 16

    def test_minimum_capacity_enforcement(self):
        """Test that capacity is enforced to be at least MIN_CAPACITY."""
        deque = CircularDeque(capacity=4)

        assert deque._capacity == CircularDeque.MIN_CAPACITY

    def test_bool_empty_deque(self):
        """Test that empty deque evaluates to False."""
        deque = CircularDeque()

        assert not deque
        assert bool(deque) is False

    def test_bool_non_empty_deque(self):
        """Test that non-empty deque evaluates to True."""
        deque = CircularDeque()

        deque.append(1)
        assert deque
        assert bool(deque) is True


class TestCircularDequeAppend:
    """Test append and appendleft operations."""

    def test_append_single_item(self):
        """Test appending a single item."""
        deque = CircularDeque()

        deque.append(1)

        assert len(deque) == 1
        assert deque.peek_rear() == 1

    def test_appendleft_single_item(self):
        """Test appending a single item to the front."""
        deque = CircularDeque()

        deque.appendleft(1)

        assert len(deque) == 1
        assert deque.peek_front() == 1

    def test_append_multiple_items(self):
        """Test appending multiple items."""
        deque = CircularDeque()

        for i in range(5):
            deque.append(i)

        assert len(deque) == 5
        assert list(deque) == [0, 1, 2, 3, 4]

    def test_appendleft_multiple_items(self):
        """Test appending multiple items to the front."""
        deque = CircularDeque()

        for i in range(5):
            deque.appendleft(i)

        assert len(deque) == 5
        assert list(deque) == [4, 3, 2, 1, 0]

    def test_mixed_append_operations(self):
        """Test mixing append and appendleft operations."""
        deque = CircularDeque()

        deque.append(1)
        deque.appendleft(0)
        deque.append(2)
        deque.appendleft(-1)

        assert list(deque) == [-1, 0, 1, 2]

    def test_append_triggers_resize(self):
        """Test that appending triggers resize when capacity is reached."""
        deque = CircularDeque(capacity=8)

        for i in range(9):
            deque.append(i)

        assert len(deque) == 9
        assert deque._capacity > 8
        assert list(deque) == list(range(9))

    def test_appendleft_triggers_resize(self):
        """Test that appendleft triggers resize when capacity is reached."""
        deque = CircularDeque(capacity=8)

        for i in range(9):
            deque.appendleft(i)

        assert len(deque) == 9
        assert deque._capacity > 8


class TestCircularDequePop:
    """Test pop and popleft operations."""

    def test_pop_single_item(self):
        """Test popping a single item."""
        deque = CircularDeque()

        deque.append(42)
        item = deque.pop()

        assert item == 42
        assert len(deque) == 0
        assert deque.is_empty()

    def test_popleft_single_item(self):
        """Test popping a single item from the front."""
        deque = CircularDeque()

        deque.append(42)
        item = deque.popleft()

        assert item == 42
        assert len(deque) == 0

    def test_pop_multiple_items(self):
        """Test popping multiple items."""
        deque = CircularDeque()

        for i in range(5):
            deque.append(i)

        items = []
        while not deque.is_empty():
            items.append(deque.pop())

        assert items == [4, 3, 2, 1, 0]

    def test_popleft_multiple_items(self):
        """Test popping multiple items from the front."""
        deque = CircularDeque()

        for i in range(5):
            deque.append(i)

        items = []
        while not deque.is_empty():
            items.append(deque.popleft())

        assert items == [0, 1, 2, 3, 4]

    def test_pop_empty_deque_raises_error(self):
        """Test that popping from empty deque raises IndexError."""
        deque = CircularDeque()

        with pytest.raises(IndexError, match="pop from empty deque"):
            deque.pop()

    def test_popleft_empty_deque_raises_error(self):
        """Test that popping from empty deque raises IndexError."""
        deque = CircularDeque()

        with pytest.raises(IndexError, match="pop from empty deque"):
            deque.popleft()

    def test_mixed_pop_operations(self):
        """Test mixing pop and popleft operations."""
        deque = CircularDeque()

        for i in range(5):
            deque.append(i)  # [0, 1, 2, 3, 4]

        assert deque.pop() == 4       # [0, 1, 2, 3]
        assert deque.popleft() == 0   # [1, 2, 3]
        assert deque.pop() == 3       # [1, 2]
        assert deque.popleft() == 1   # [2]
        assert deque.pop() == 2       # []
        assert deque.is_empty()


class TestCircularDequePeek:
    """Test peek operations."""

    def test_peek_front(self):
        """Test peeking at front item."""
        deque = CircularDeque()

        deque.append(1)
        deque.append(2)

        assert deque.peek_front() == 1
        assert len(deque) == 2  # Ensure no modification

    def test_peek_rear(self):
        """Test peeking at rear item."""
        deque = CircularDeque()

        deque.append(1)
        deque.append(2)

        assert deque.peek_rear() == 2
        assert len(deque) == 2  # Ensure no modification

    def test_peek_front_empty_raises_error(self):
        """Test that peeking front on empty deque raises IndexError."""
        deque = CircularDeque()

        with pytest.raises(IndexError, match="peek from empty deque"):
            deque.peek_front()

    def test_peek_rear_empty_raises_error(self):
        """Test that peeking rear on empty deque raises IndexError."""
        deque = CircularDeque()

        with pytest.raises(IndexError, match="peek from empty deque"):
            deque.peek_rear()

    def test_peek_after_operations(self):
        """Test peek operations after various modifications."""
        deque = CircularDeque()

        deque.append(1)
        deque.appendleft(0)
        deque.append(2)

        assert deque.peek_front() == 0
        assert deque.peek_rear() == 2

        deque.popleft()
        assert deque.peek_front() == 1


class TestCircularDequeResize:
    """Test automatic resizing behavior."""

    def test_growth_on_append(self):
        """Test that deque grows when capacity is reached."""
        initial_capacity = 8
        deque = CircularDeque(capacity=initial_capacity)

        for i in range(initial_capacity + 1):
            deque.append(i)

        assert deque._capacity == initial_capacity * CircularDeque.GROWTH_FACTOR
        assert list(deque) == list(range(initial_capacity + 1))

    def test_shrink_on_pop(self):
        """Test that deque shrinks when utilization is low."""
        deque = CircularDeque(capacity=32)

        # Fill the deque
        for i in range(32):
            deque.append(i)

        # Remove items to trigger shrinking
        for _ in range(28):
            deque.pop()

        # Should shrink when size <= capacity * 0.25
        assert deque._capacity < 32
        assert len(deque) == 4

    def test_minimum_capacity_on_shrink(self):
        """Test that capacity never goes below MIN_CAPACITY."""
        deque = CircularDeque()

        # Add and remove many items
        for i in range(100):
            deque.append(i)

        for _ in range(99):
            deque.pop()

        assert deque._capacity >= CircularDeque.MIN_CAPACITY
        assert len(deque) == 1

    def test_resize_maintains_order(self):
        """Test that resizing maintains element order."""
        deque = CircularDeque(capacity=8)

        # Create a wrapped state
        for i in range(5):
            deque.append(i)

        deque.popleft()
        deque.popleft()
        deque.append(5)
        deque.append(6)
        deque.append(7)
        deque.append(8)

        # This should trigger a resize
        deque.append(9)

        assert list(deque) == [2, 3, 4, 5, 6, 7, 8, 9]


class TestCircularDequeIndexing:
    """Test indexing and iteration."""

    def test_positive_indexing(self):
        """Test accessing items by positive index."""
        deque = CircularDeque()

        for i in range(5):
            deque.append(i)

        assert deque[0] == 0
        assert deque[2] == 2
        assert deque[4] == 4

    def test_negative_indexing(self):
        """Test accessing items by negative index."""
        deque = CircularDeque()

        for i in range(5):
            deque.append(i)

        assert deque[-1] == 4
        assert deque[-2] == 3
        assert deque[-5] == 0

    def test_index_out_of_range(self):
        """Test that invalid indices raise IndexError."""
        deque = CircularDeque()

        for i in range(5):
            deque.append(i)

        with pytest.raises(IndexError, match="deque index out of range"):
            _ = deque[5]

        with pytest.raises(IndexError, match="deque index out of range"):
            _ = deque[-6]

    def test_indexing_empty_deque(self):
        """Test that indexing empty deque raises IndexError."""
        deque = CircularDeque()

        with pytest.raises(IndexError):
            _ = deque[0]

    def test_iteration(self):
        """Test iterating over deque elements."""
        deque = CircularDeque()
        items = [1, 2, 3, 4, 5]

        for item in items:
            deque.append(item)

        assert list(deque) == items

    def test_iteration_empty_deque(self):
        """Test iterating over empty deque."""
        deque = CircularDeque()
        assert list(deque) == []

    def test_iteration_after_wrap_around(self):
        """Test iteration when internal array has wrapped."""
        deque = CircularDeque(capacity=8)

        # Create wrapped state
        for i in range(5):
            deque.append(i)
        for _ in range(3):
            deque.popleft()
        for i in range(5, 10):
            deque.append(i)

        assert list(deque) == [3, 4, 5, 6, 7, 8, 9]


class TestCircularDequeClear:
    """Test clear operation."""

    def test_clear_empty_deque(self):
        """Test clearing an empty deque."""
        deque = CircularDeque()

        deque.clear()

        assert len(deque) == 0
        assert deque.is_empty()

    def test_clear_non_empty_deque(self):
        """Test clearing a non-empty deque."""
        deque = CircularDeque()

        for i in range(10):
            deque.append(i)

        deque.clear()

        assert len(deque) == 0
        assert deque.is_empty()
        assert deque._capacity == CircularDeque.MIN_CAPACITY

    def test_clear_resets_capacity(self):
        """Test that clear resets capacity to MIN_CAPACITY."""
        deque = CircularDeque(capacity=64)

        for i in range(50):
            deque.append(i)

        deque.clear()
        assert deque._capacity == CircularDeque.MIN_CAPACITY

    def test_operations_after_clear(self):
        """Test that deque works correctly after clear."""
        deque = CircularDeque()

        for i in range(5):
            deque.append(i)

        deque.clear()
        deque.append(10)
        deque.appendleft(5)

        assert list(deque) == [5, 10]


class TestCircularDequeStringRepresentation:
    """Test string representation methods."""

    def test_str_empty_deque(self):
        """Test string representation of empty deque."""
        deque = CircularDeque()

        assert str(deque) == "Deque([])"

    def test_str_non_empty_deque(self):
        """Test string representation of non-empty deque."""
        deque = CircularDeque()

        deque.append(1)
        deque.append(2)
        deque.append(3)

        assert str(deque) == "Deque([1, 2, 3])"

    def test_repr_equals_str(self):
        """Test that repr equals str."""
        deque = CircularDeque()

        deque.append(1)

        assert repr(deque) == str(deque)

    def test_str_with_strings(self):
        """Test string representation with string items."""
        deque = CircularDeque()

        deque.append("hello")
        deque.append("world")

        assert str(deque) == "Deque(['hello', 'world'])"


class TestCircularDequeEdgeCases:
    """Test edge cases and special scenarios."""

    def test_single_element_operations(self):
        """Test all operations on single element."""
        deque = CircularDeque()

        deque.append(42)

        assert deque.peek_front() == 42
        assert deque.peek_rear() == 42
        assert deque[0] == 42
        assert deque[-1] == 42
        assert len(deque) == 1

    def test_alternating_append_pop(self):
        """Test alternating append and pop operations."""
        deque = CircularDeque()

        for i in range(100):
            deque.append(i)
            if i % 2 == 1:
                deque.popleft()

        assert len(deque) == 50

    def test_queue_behavior(self):
        """Test using deque as a queue (FIFO)."""
        deque = CircularDeque()

        # Enqueue
        for i in range(5):
            deque.append(i)

        # Dequeue
        items = []
        while not deque.is_empty():
            items.append(deque.popleft())

        assert items == [0, 1, 2, 3, 4]

    def test_stack_behavior(self):
        """Test using deque as a stack (LIFO)."""
        deque = CircularDeque()

        # Push
        for i in range(5):
            deque.append(i)

        # Pop
        items = []
        while not deque.is_empty():
            items.append(deque.pop())

        assert items == [4, 3, 2, 1, 0]

    def test_large_number_of_operations(self):
        """Test with a large number of operations."""
        deque = CircularDeque()

        # Add many items
        for i in range(1000):
            deque.append(i)

        # Remove half
        for _ in range(500):
            deque.popleft()

        # Add more
        for i in range(1000, 1500):
            deque.append(i)

        assert len(deque) == 1000
        assert deque.peek_front() == 500
        assert deque.peek_rear() == 1499

    def test_type_flexibility(self):
        """Test that deque works with different types."""
        # Strings
        deque_str = CircularDeque()

        deque_str.append("a")
        deque_str.append("b")

        assert list(deque_str) == ["a", "b"]

        # Mixed types (though not type-safe)
        deque_mixed = CircularDeque()

        deque_mixed.append(1)
        deque_mixed.append("two")
        deque_mixed.append(3.0)

        assert len(deque_mixed) == 3

    def test_circular_wrap_around(self):
        """Test behavior with circular wrap-around."""
        deque = CircularDeque(capacity=8)

        # Fill partially
        for i in range(5):
            deque.append(i)

        # Remove from front to create space
        deque.popleft()
        deque.popleft()

        # Add more to wrap around
        for i in range(5, 10):
            deque.append(i)

        # Verify order is maintained
        assert list(deque) == [2, 3, 4, 5, 6, 7, 8, 9]
        assert deque[0] == 2
        assert deque[-1] == 9


class TestCircularDequeMemoryManagement:
    """Test memory management and cleanup."""

    def test_none_cleanup_on_pop(self):
        """Test that popped slots are set to None."""
        deque = CircularDeque()

        deque.append(1)
        deque.append(2)

        deque.pop()

        # The back slot should be None
        back_index = (deque._front + deque._size) % deque._capacity
        assert deque._data[back_index] is None

    def test_none_cleanup_on_popleft(self):
        """Test that popped slots are set to None on popleft."""
        deque = CircularDeque()
        deque.append(1)
        deque.append(2)

        old_front = deque._front
        deque.popleft()

        # The old front slot should be None
        assert deque._data[old_front] is None
