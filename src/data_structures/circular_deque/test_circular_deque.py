import pytest
from circular_deque import CircularDeque


class TestCircularDequeBasics:
    """Test basic deque operations."""

    def test_initialization(self):
        """Test deque is properly initialized."""
        deque: CircularDeque[int] = CircularDeque()

        assert len(deque) == 0
        assert deque.is_empty()

    def test_custom_capacity(self):
        """Test initialization with custom capacity."""
        deque: CircularDeque[str] = CircularDeque(capacity=16)

        assert deque._capacity == 16
        assert len(deque) == 0


class TestAppendOperations:
    """Test append operations at both ends."""

    def test_append_right_single(self):
        """Test appending a single element to the right."""
        deque: CircularDeque[int] = CircularDeque()

        deque.append(1)

        assert len(deque) == 1
        assert not deque.is_empty()
        assert deque.peek_rear() == 1

    def test_append_left_single(self):
        """Test appending a single element to the left."""
        deque: CircularDeque[int] = CircularDeque()

        deque.appendleft(1)

        assert len(deque) == 1
        assert deque.peek_front() == 1

    def test_append_right_multiple(self):
        """Test appending multiple elements to the right."""
        deque: CircularDeque[int] = CircularDeque()

        for i in range(5):
            deque.append(i)

        assert len(deque) == 5
        assert deque.peek_front() == 0
        assert deque.peek_rear() == 4

    def test_append_left_multiple(self):
        """Test appending multiple elements to the left."""
        deque: CircularDeque[int] = CircularDeque()

        for i in range(5):
            deque.appendleft(i)

        assert len(deque) == 5
        assert deque.peek_front() == 4
        assert deque.peek_rear() == 0

    def test_append_both_ends(self):
        """Test appending to both ends."""
        deque: CircularDeque[int] = CircularDeque()

        deque.append(1)
        deque.appendleft(0)
        deque.append(2)
        deque.appendleft(-1)

        assert len(deque) == 4
        assert deque.peek_front() == -1
        assert deque.peek_rear() == 2


class TestStringRepresentation:
    """Test string representation methods."""

    def test_str_empty(self):
        """Test string representation of empty deque."""
        deque: CircularDeque[int] = CircularDeque()

        assert str(deque) == "Deque([])"

    def test_str_with_elements(self):
        """Test string representation with elements."""
        deque: CircularDeque[int] = CircularDeque()

        deque.append(1)
        deque.append(2)
        deque.appendleft(0)

        assert str(deque) == "Deque([0, 1, 2])"

    def test_repr(self):
        """Test repr matches str."""
        deque: CircularDeque[int] = CircularDeque()

        deque.append(1)

        assert repr(deque) == str(deque)
