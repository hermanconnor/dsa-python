from typing import Generic, TypeVar, Optional, List, Callable, Any

T = TypeVar('T')
K = TypeVar('K', bound=Any)


class MinHeap(Generic[T]):
    def __init__(self, key: Optional[Callable[[T], K]] = None) -> None:
        """
        Initialize an empty min heap with optional key function.

        Args:
            key: Optional function to extract comparison key from elements.
                 If None, elements are compared directly.

        Time complexity: O(1)
        """
        self.heap: List[T] = []
        self.key: Callable[[T], K] = key if key else lambda x: x

    def parent(self, index: int) -> int:
        """
        Get the parent index of a node.

        Time complexity: O(1)
        """
        return (index - 1) // 2

    def left_child(self, index: int) -> int:
        """
        Get the left child index of a node.

        Time complexity: O(1)
        """
        return 2 * index + 1

    def right_child(self, index: int) -> int:
        """
        Get the right child index of a node.

        Time complexity: O(1)
        """
        return 2 * index + 2

    def has_parent(self, index: int) -> bool:
        """
        Check if a node has a parent.

        Time complexity: O(1)
        """
        return self.parent(index) >= 0

    def has_left_child(self, index: int) -> bool:
        """
        Check if a node has a left child.

        Time complexity: O(1)
        """
        return self.left_child(index) < len(self.heap)

    def has_right_child(self, index: int) -> bool:
        """
        Check if a node has a right child.

        Time complexity: O(1)
        """
        return self.right_child(index) < len(self.heap)

    def peek(self) -> T:
        """
        Return the minimum element (root) without removing it.

        Returns:
            The minimum element in the heap.

        Raises:
            IndexError: If the heap is empty.

        Time complexity: O(1)
        """
        if not self.heap:
            raise IndexError("Heap is empty")

        return self.heap[0]

    def insert(self, value: T) -> None:
        """
        Insert a new value into the heap.

        Args:
            value: The value to insert.

        Time complexity: O(log n) where n is the number of elements in the heap.
        """
        self.heap.append(value)
        self._heapify_up()

    def _swap(self, index1: int, index2: int) -> None:
        """
        Swap two elements in the heap.

        Time complexity: O(1)
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _heapify_up(self, index: Optional[int] = None) -> None:
        """
        Bubble up an element to maintain heap property.

        Args:
            index: Starting index (defaults to last element).

        Time complexity: O(log n) where n is the number of elements in the heap.
        """
        if index is None:
            index = len(self.heap) - 1

        while (self.has_parent(index) and
               self.key(self.heap[index]) < self.key(self.heap[self.parent(index)])):
            self._swap(index, self.parent(index))
            index = self.parent(index)

    def _heapify_down(self, index: int = 0) -> None:
        """
        Bubble down from a specific index to maintain heap property.

        Args:
            index: Starting index (defaults to root).

        Time complexity: O(log n) where n is the number of elements in the heap.
        """
        element_to_sift = self.heap[index]
        key_to_sift = self.key(element_to_sift)

        while self.has_left_child(index):
            smaller_child_index = self.left_child(index)

            if (self.has_right_child(index) and
                    self.key(self.heap[self.right_child(index)]) < self.key(self.heap[smaller_child_index])):
                smaller_child_index = self.right_child(index)

            if key_to_sift <= self.key(self.heap[smaller_child_index]):
                break

            self._swap(index, smaller_child_index)
            index = smaller_child_index

    def build_heap(self, arr: List[T]) -> None:
        """
        Build a heap from an array of values.

        Args:
            arr: List of values to build the heap from.

        Time complexity: O(n) where n is the number of elements in the array.
        """
        self.heap = arr.copy()

        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def extract_min(self) -> T:
        """
        Remove and return the minimum element (root).

        Returns:
            The minimum element in the heap.

        Raises:
            IndexError: If the heap is empty.

        Time complexity: O(log n) where n is the number of elements in the heap.
        """
        if not self.heap:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._heapify_down()

        return min_value

    def replace(self, value: T) -> T:
        """
        Pop minimum and insert new value in one operation.
        More efficient than calling extract_min() followed by insert().

        Args:
            value: The new value to insert.

        Returns:
            The minimum element that was removed.

        Raises:
            IndexError: If the heap is empty.

        Time complexity: O(log n) where n is the number of elements in the heap.
        """
        if not self.heap:
            raise IndexError("Heap is empty")

        min_value = self.heap[0]
        self.heap[0] = value
        self._heapify_down()

        return min_value

    def __len__(self) -> int:
        """
        Return the number of elements in the heap.

        Time complexity: O(1)
        """
        return len(self.heap)

    def __bool__(self) -> bool:
        """
        Return True if the heap is not empty, False otherwise.

        Time complexity: O(1)
        """
        return bool(self.heap)

    def __iter__(self):
        """
        Iterate over heap elements (not in sorted order).

        Time complexity: O(1) to create iterator, O(n) to iterate all elements.
        """
        return iter(self.heap)

    def __str__(self) -> str:
        """
        String representation of the heap.

        Time complexity: O(n) where n is the number of elements.
        """
        return str(self.heap)

    def __repr__(self) -> str:
        """
        Developer-friendly representation.

        Time complexity: O(n) where n is the number of elements.
        """
        return f"MinHeap({self.heap})"
