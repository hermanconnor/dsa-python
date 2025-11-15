from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')


class CircularDeque(Generic[T]):
    """
      A Deque (double-ended queue) implementation using a circular array.
      Supports O(1) operations at both ends with dynamic resizing.
    """

    def __init__(self, capacity: int = 8) -> None:
        """
        Initialize the deque with a given capacity.
        """
        self._capacity = capacity
        self._data: List[Optional[T]] = [None] * capacity
        self._front = 0
        self._size = 0

        def appendleft(self, item: T) -> None:
            """
            Add an item to the front of the deque.

            Time Complexity: O(1) amortized, O(n) worst case when resizing
            Space Complexity: O(1) amortized
            """
            pass

        def append(self, item: T) -> None:
            """
            Add an item to the back of the deque.

            Time Complexity: O(1) amortized, O(n) worst case when resizing
            Space Complexity: O(1) amortized
            """
            pass

        def popleft(self) -> T:
            """
            Remove and return an item from the front of the deque.

            Time Complexity: O(1) amortized
            Space Complexity: O(1)
            Raises: IndexError if deque is empty
            """
            pass

        def pop(self) -> T:
            """
            Remove and return an item from the back of the deque.

            Time Complexity: O(1) amortized
            Space Complexity: O(1)
            Raises: IndexError if deque is empty
            """
            pass

        def peek_front(self) -> T:
            """
            Return the front item without removing it.

            Time Complexity: O(1)
            Space Complexity: O(1)
            Raises: IndexError if deque is empty
            """
            pass

        def peek_rear(self) -> T:
            """
            Return the back item without removing it.

            Time Complexity: O(1)
            Space Complexity: O(1)
            Raises: IndexError if deque is empty
            """
            pass

        def is_empty(self) -> bool:
            """
            Check if the deque is empty.

            Time Complexity: O(1)
            Space Complexity: O(1)
            """
            pass

        def _resize(self, new_capacity: int) -> None:
            """
            Resize the internal array to a new capacity.

            Time Complexity: O(n) where n is the number of elements
            Space Complexity: O(new_capacity)
            """
            pass

        def __len__(self) -> int:
            """
            Return the number of items in the deque.

            Time Complexity: O(1)
            Space Complexity: O(1)
            """
            pass

        def __str__(self) -> str:
            """
            String representation of the deque.

            Time Complexity: O(n)
            Space Complexity: O(n)
            """
            pass

        def __repr__(self) -> str:
            """Developer-friendly representation of the circular deque O(n)."""
            pass
