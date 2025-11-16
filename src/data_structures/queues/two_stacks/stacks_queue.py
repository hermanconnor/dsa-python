from typing import Generic, TypeVar, Deque
from collections import deque


T = TypeVar('T')


class StacksQueue(Generic[T]):
    """
    A Queue implementation using two stacks (represented by collections.deque).

    The key insight is using one stack for enqueue operations and another
    for dequeue operations, transferring elements lazily only when needed.
    """

    def __init__(self) -> None:
        """
        Initialize the queue with two empty deques (stacks).

        Time Complexity: O(1)
        """
        self._enqueue_stack: Deque[T] = deque()
        self._dequeue_stack: Deque[T] = deque()

    def enqueue(self, item: T) -> None:
        """
        Add an item to the back of the queue.

        Args:
            item: The item to add

        Time Complexity: O(1)
        """
        self._enqueue_stack.append(item)

    def dequeue(self) -> T:
        """
        Remove and return the item at the front of the queue.

        Time Complexity: O(1) amortized
        """
        self._transfer_if_needed()

        if not self._dequeue_stack:
            raise IndexError("dequeue from empty queue")

        return self._dequeue_stack.pop()

    def peek(self) -> T:
        """
        Return the item at the front of the queue without removing it.

        Time Complexity: O(1) amortized
        """
        self._transfer_if_needed()

        if not self._dequeue_stack:
            raise IndexError("peek from empty queue")

        return self._dequeue_stack[-1]

    def _transfer_if_needed(self) -> None:
        """
        Transfer elements from enqueue_stack to dequeue_stack if needed.

        Time Complexity: O(n) where n is the size of enqueue_stack.
        """
        if not self._dequeue_stack:
            while self._enqueue_stack:
                self._dequeue_stack.append(self._enqueue_stack.pop())

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise

        Time Complexity: O(1)
        """
        return not (self._enqueue_stack or self._dequeue_stack)

    def __len__(self) -> int:
        """
        Return the number of items in the queue.

        Time Complexity: O(1)
        """
        return len(self._enqueue_stack) + len(self._dequeue_stack)

    def __bool__(self) -> bool:
        """
        Check if the queue is not empty. Allows 'if queue:' checks.

        Time Complexity: O(1)
        """
        return not self.is_empty()

    def __str__(self) -> str:
        """
        Return a string representation of the queue.

        Format: "Queue([front, ..., back])"

        Time Complexity: O(n)
        """
        # Build the queue in order: dequeue_stack (reversed) + enqueue_stack
        items = list(reversed(self._dequeue_stack)) + list(self._enqueue_stack)
        return f"Queue({items})"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the queue.

        Time Complexity: O(n)
        """
        return (f"StacksQueue(size={len(self)}, "
                f"enqueue_stack={list(self._enqueue_stack)}, "
                f"dequeue_stack={list(self._dequeue_stack)})")
