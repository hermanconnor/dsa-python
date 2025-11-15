from typing import Generic, TypeVar, List, Optional, Iterator

T = TypeVar('T')


class CircularDeque(Generic[T]):
    """
    A Deque (double-ended queue) implementation using a circular array.
    Supports O(1) operations at both ends with dynamic resizing.
    """

    MIN_CAPACITY = 8
    GROWTH_FACTOR = 2
    SHRINK_THRESHOLD = 0.25

    def __init__(self, capacity: int = 8) -> None:
        """
        Initialize the deque with a given capacity.
        Capacity will be automatically enforced to be at least MIN_CAPACITY.

        Args:
            capacity: Initial capacity (minimum MIN_CAPACITY)

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

        Args:
            item: The item to add

        Time Complexity: O(1) amortized, O(n) worst case when resizing
        Space Complexity: O(1) amortized
        """
        if self._size == self._capacity:
            self._resize(self._capacity * self.GROWTH_FACTOR)

        self._front = (self._front - 1) % self._capacity
        self._data[self._front] = item
        self._size += 1

    def append(self, item: T) -> None:
        """
        Add an item to the back of the deque.

        Args:
            item: The item to add

        Time Complexity: O(1) amortized, O(n) worst case when resizing
        Space Complexity: O(1) amortized
        """
        if self._size == self._capacity:
            self._resize(self._capacity * self.GROWTH_FACTOR)

        back_index = (self._front + self._size) % self._capacity
        self._data[back_index] = item
        self._size += 1

    def popleft(self) -> T:
        """
        Remove and return an item from the front of the deque.

        Returns:
            The item from the front of the deque

        Raises:
            IndexError: If deque is empty

        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty deque")

        item = self._data[self._front]
        assert item is not None, "Internal error: expected non-None item"

        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1

        self._shrink_if_needed()

        return item

    def pop(self) -> T:
        """
        Remove and return an item from the back of the deque.

        Returns:
            The item from the back of the deque

        Raises:
            IndexError: If deque is empty

        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty deque")

        back_index = (self._front + self._size - 1) % self._capacity
        item = self._data[back_index]
        assert item is not None, "Internal error: expected non-None item"

        self._data[back_index] = None
        self._size -= 1

        self._shrink_if_needed()

        return item

    def peek_front(self) -> T:
        """
        Return the front item without removing it.

        Returns:
            The item at the front of the deque

        Raises:
            IndexError: If deque is empty

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from empty deque")

        item = self._data[self._front]
        assert item is not None, "Internal error: expected non-None item"

        return item

    def peek_rear(self) -> T:
        """
        Return the back item without removing it.

        Returns:
            The item at the back of the deque

        Raises:
            IndexError: If deque is empty

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from empty deque")

        back_index = (self._front + self._size - 1) % self._capacity
        item = self._data[back_index]
        assert item is not None, "Internal error: expected non-None item"

        return item

    def clear(self) -> None:
        """
        Remove all items from the deque and reset to initial capacity.

        Time Complexity: O(1)
        Space Complexity: O(MIN_CAPACITY)
        """
        self._capacity = self.MIN_CAPACITY
        self._data = [None] * self._capacity
        self._front = 0
        self._size = 0

    def is_empty(self) -> bool:
        """
        Check if the deque is empty.

        Returns:
            True if the deque is empty, False otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size == 0

    def _shrink_if_needed(self) -> None:
        """
        Shrink the internal array if utilization is too low.
        Maintains minimum capacity of MIN_CAPACITY.

        Time Complexity: O(n) when shrinking occurs, O(1) otherwise
        Space Complexity: O(1)
        """
        if (self._size > 0 and
            self._capacity > self.MIN_CAPACITY and
                self._size <= self._capacity * self.SHRINK_THRESHOLD):

            new_capacity = max(self._capacity // 2, self.MIN_CAPACITY)
            self._resize(new_capacity)

    def _resize(self, new_capacity: int) -> None:
        """
        Resize the internal array to a new capacity.
        Ensures capacity is never below MIN_CAPACITY.

        Args:
            new_capacity: The target capacity

        Time Complexity: O(n) where n is the number of elements
        Space Complexity: O(new_capacity)
        """
        new_capacity = max(new_capacity, self.MIN_CAPACITY)

        if new_capacity == self._capacity:
            return

        new_data: List[Optional[T]] = [None] * new_capacity

        for i in range(self._size):
            new_data[i] = self._data[(self._front + i) % self._capacity]

        self._data = new_data
        self._front = 0
        self._capacity = new_capacity

    def __len__(self) -> int:
        """
        Return the number of items in the deque.

        Returns:
            The number of items in the deque

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size

    def __iter__(self) -> Iterator[T]:
        """
        Allow iteration over the deque elements from front to back.

        Yields:
            Each item in the deque from front to back

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(self._size):
            item = self._data[(self._front + i) % self._capacity]
            assert item is not None, "Internal error: expected non-None item"
            yield item

    def __getitem__(self, index: int) -> T:
        """
        Support indexing (e.g., deque[0] for front, deque[-1] for back).

        Args:
            index: The index to access (supports negative indexing)

        Returns:
            The item at the specified index

        Raises:
            IndexError: If index is out of range

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if index < 0:
            index += self._size

        if not (0 <= index < self._size):
            raise IndexError("deque index out of range")

        array_index = (self._front + index) % self._capacity
        item = self._data[array_index]
        assert item is not None, "Internal error: expected non-None item"

        return item

    def __str__(self) -> str:
        """
        String representation: Deque([item1, item2, ...])

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        items_str = ", ".join(repr(item) for item in self)
        return f"Deque([{items_str}])"

    def __repr__(self) -> str:
        """
        Developer-friendly representation of the circular deque.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return self.__str__()

    def __bool__(self) -> bool:
        """
        Support truth value testing (e.g., if deque:).

        Returns:
            False if deque is empty, True otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return not self.is_empty()
