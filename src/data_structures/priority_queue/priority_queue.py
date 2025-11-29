import heapq
import itertools
from typing import Generic, TypeVar, Optional, List, Dict, Tuple, Iterator

T = TypeVar('T')


class PriorityQueue(Generic[T]):
    """
    A Min-Priority Queue implementation using the built-in 'heapq' module.
    Items are stored as (priority, index, item) tuples.
    Supports lazy deletion for efficient priority updates.
    """

    REMOVED: str = '<removed-item>'

    def __init__(self, items: Optional[List[Tuple[T, float]]] = None) -> None:
        """
        Initialize an empty priority queue or with initial items.

        Args:
            items: Optional list of (item, priority) tuples

        Time Complexity: O(n) if items provided, O(1) otherwise
        """
        self._heap: List[Tuple[float, int, T]] = []
        self._counter: Iterator[int] = itertools.count()
        self._entry_finder: Dict[T, List] = {}

        if items:
            for item, priority in items:
                self.push(item, priority)

    def push(self, item: T, priority: float) -> None:
        """
        Add a new item or update the priority of an existing item.
        If the item already exists, it marks the old entry as removed
        and adds a new entry with the updated priority.

        Args:
            item: The item to add
            priority: The priority value (lower values = higher priority)

        Time Complexity: O(log n)
        """
        # If item already exists, mark it as removed
        if item in self._entry_finder:
            self.remove(item)

        # Get the next unique index for the tie-breaker
        index = next(self._counter)
        # Create the entry as a list so we can mark it as removed later
        entry = [priority, index, item]
        self._entry_finder[item] = entry
        # Push the entry onto the heap
        heapq.heappush(self._heap, entry)

    def pop(self) -> T:
        """
        Remove and return the item with the highest priority (lowest value).
        Skips over any items that have been marked as removed.

        Returns:
            The item with the highest priority

        Raises:
            IndexError: If the queue is empty

        Time Complexity: O(log n) amortized
        """
        while self._heap:
            _, _, item = heapq.heappop(self._heap)

            if item is not self.REMOVED:
                del self._entry_finder[item]
                return item

        raise IndexError("pop from empty priority queue")

    def peek(self) -> T:
        """
        Return the item with the highest priority without removing it.

        Returns:
            The item with the highest priority

        Raises:
            IndexError: If the queue is empty

        Time Complexity: O(1) best case, O(n) worst case if many removed items
        """
        while self._heap:
            _, _, item = self._heap[0]

            if item is not self.REMOVED:
                return item
            heapq.heappop(self._heap)

        raise IndexError("peek from empty priority queue")

    def remove(self, item: T) -> None:
        """
        Mark an existing item as removed. The actual removal happens lazily.

        Args:
            item: The item to remove

        Raises:
            KeyError: If the item is not in the queue

        Time Complexity: O(1)
        """
        entry = self._entry_finder.pop(item)
        entry[-1] = self.REMOVED

    def update_priority(self, item: T, new_priority: float) -> None:
        """
        Update the priority of an existing item or add it if not present.
        This is an alias for push() for semantic clarity.

        Args:
            item: The item to update
            new_priority: The new priority value

        Time Complexity: O(log n)
        """
        self.push(item, new_priority)

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise

        Time Complexity: O(1) best case, O(n) worst case if all items removed
        """
        while self._heap:
            if self._heap[0][2] is not self.REMOVED:
                return False
            heapq.heappop(self._heap)

        return True

    def clear(self) -> None:
        """
        Remove all items from the queue.

        Time Complexity: O(1)
        """
        self._heap.clear()
        self._entry_finder.clear()
        self._counter = itertools.count()

    def __len__(self) -> int:
        """
        Return the number of valid items in the queue.
        Note: This counts only non-removed items.

        Time Complexity: O(n) - must check all entries
        """
        return sum(1 for entry in self._heap if entry[2] is not self.REMOVED)

    def __bool__(self) -> bool:
        """
        Return True if the queue is non-empty.

        Time Complexity: O(1) best case, O(n) worst case if all items removed
        """
        return not self.is_empty()

    def __contains__(self, item: T) -> bool:
        """
        Check if an item is in the queue.

        Args:
            item: The item to check

        Returns:
            True if the item is in the queue, False otherwise

        Time Complexity: O(1)
        """
        return item in self._entry_finder

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the queue.
        Shows items in priority order (lowest priority value first).

        Time Complexity: O(n log n)
        """
        if self.is_empty():
            return "PriorityQueue(empty)"

        # Get all valid items and sort by priority
        valid_items = [(p, item) for p, _, item in self._heap
                       if item is not self.REMOVED]
        valid_items.sort()

        items_str = ", ".join(f"{item}(p={p})" for p, item in valid_items)
        return f"PriorityQueue([{items_str}])"

    def __repr__(self) -> str:
        """
        Return a detailed representation of the queue.

        Time Complexity: O(n)
        """
        valid_items = [(p, item) for p, _, item in self._heap
                       if item is not self.REMOVED]
        return f"PriorityQueue({valid_items})"
