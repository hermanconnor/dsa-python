from typing import Generic, TypeVar, List, Optional, Iterator

T = TypeVar('T')


class CircularDeque(Generic[T]):
    """
      A Deque (double-ended queue) implementation using a circular array.
      Supports O(1) operations at both ends with dynamic resizing.
    """

    MIN_CAPACITY = 8

    def __init__(self, capacity: int = MIN_CAPACITY) -> None:
        """
        Initialize the deque with a given capacity. Capacity will be 
        automatically enforced to be at least MIN_CAPACITY.

        Time Complexity: O(1)
        Space Complexity: O(capacity)
        """
        self._capacity = max(capacity, self.MIN_CAPACITY)
        self._data: List[Optional[T]] = [None] * self._capacity
        self._front = 0
        self._size = 0

    def appendleft(self, item: T) -> None:
        """
        Add an item to the front of the deque.

        Time Complexity: O(1) amortized, O(n) worst case when resizing
        Space Complexity: O(1) amortized
        """
        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        self._front = (self._front - 1) % self._capacity
        self._data[self._front] = item
        self._size += 1

    def append(self, item: T) -> None:
        """
        Add an item to the back of the deque.

        Time Complexity: O(1) amortized, O(n) worst case when resizing
        Space Complexity: O(1) amortized
        """
        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        # Calculate back index (where the new item goes)
        back_index = (self._front + self._size) % self._capacity
        self._data[back_index] = item
        self._size += 1

    def popleft(self) -> T:
        """
        Remove and return an item from the front of the deque.

        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        Raises: IndexError if deque is empty
        """
        if self.is_empty():
            raise IndexError("pop from empty deque")

        item = self._data[self._front]
        # We assert item is not None because we check self.is_empty()
        assert item is not None

        # Set the old slot to None for proper garbage collection
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1

        self._check_and_shrink()

        return item

    def pop(self) -> T:
        """
        Remove and return an item from the back of the deque.

        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        Raises: IndexError if deque is empty
        """
        if self.is_empty():
            raise IndexError("pop from empty deque")

        # Calculate back index (of the element to be removed)
        back_index = (self._front + self._size - 1) % self._capacity

        item = self._data[back_index]
        assert item is not None

        # Set the old slot to None for proper garbage collection
        self._data[back_index] = None
        self._size -= 1

        self._check_and_shrink()

        return item

    def peek_front(self) -> T:
        """
        Return the front item without removing it.

        Time Complexity: O(1)
        Space Complexity: O(1)
        Raises: IndexError if deque is empty
        """
        if self.is_empty():
            raise IndentationError("peek from empty deque")

        item = self._data[self._front]
        assert item is not None

        return item

    def peek_rear(self) -> T:
        """
        Return the back item without removing it.

        Time Complexity: O(1)
        Space Complexity: O(1)
        Raises: IndexError if deque is empty
        """
        if self.is_empty():
            raise IndexError("peek from empty deque")

        back_index = (self._front + self._size - 1) % self._capacity
        item = self._data[back_index]
        assert item is not None

        return item

    def is_empty(self) -> bool:
        """
        Check if the deque is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size == 0

    def _resize(self, new_capacity: int) -> None:
        """
        Resize the internal array to a new capacity.

        Time Complexity: O(n) where n is the number of elements
        Space Complexity: O(new_capacity)
        """
        new_data: List[Optional[T]] = [None] * new_capacity

        for i in range(self._size):
            old_index = (self._front + i) % self._capacity
            new_data[i] = self._data[old_index]

        self._data = new_data
        self._front = 0
        self._capacity = new_capacity

    def _check_and_shrink(self) -> None:
        """
        Checks if the deque should shrink and performs the resize operation.
        Shrinks if capacity is 4x size, and if capacity is larger than MIN_CAPACITY.
        """
        # Shrink if size is 25% or less of capacity AND capacity is greater than min
        if self._size > 0 and \
           self._size <= self._capacity // 4 and \
           self._capacity > self.MIN_CAPACITY:

            # Ensure new capacity doesn't fall below MIN_CAPACITY
            new_capacity = max(self._capacity // 2, self.MIN_CAPACITY)

            # Only resize if the capacity is actually changing
            if new_capacity < self._capacity:
                self._resize(new_capacity)

    def __len__(self) -> int:
        """
        Return the number of items in the deque.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Allow iteration over the deque elements from front to back."""
        for i in range(self._size):
            item = self._data[(self._front + i) % self._capacity]
            assert item is not None
            yield item

    def __getitem__(self, index: int) -> T:
        """
        Support indexing (e.g., deque[0]).
        Time Complexity: O(1)
        """
        # Allow negative indexing
        if index < 0:
            index += self._size

        if not (0 <= index < self._size):
            raise IndexError("Deque index out of range")

        array_index = (self._front + index) % self._capacity
        item = self._data[array_index]
        assert item is not None
        return item

    def __str__(self) -> str:
        """String representation: Deque([item1, item2, ...])"""
        items_str = ", ".join(repr(item) for item in self)
        return f"Deque([{items_str}])"

    def __repr__(self) -> str:
        """Developer-friendly representation of the circular deque O(n)."""
        return self.__str__()
