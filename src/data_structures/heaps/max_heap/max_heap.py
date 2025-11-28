from typing import Generic, TypeVar, Optional, List, Callable, Any

T = TypeVar('T')
K = TypeVar('K', bound=Any)


class MaxHeap(Generic[T]):
    def __init__(self, key: Optional[Callable[[T], K]] = None) -> None:
        """
        Initialize an empty max heap with optional key function.

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
        Return the maximum element (root) without removing it.

        Returns:
            The maximum element in the heap.

        Raises:
            IndexError: If the heap is empty.

        Time complexity: O(1)
        """
        if not self.heap:
            raise IndexError("Heap is empty")

        return self.heap[0]

    def _swap(self, index1: int, index2: int) -> None:
        """
        Swap two elements in the heap.

        Time complexity: O(1)
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _heapify_up(self, index: Optional[int] = None) -> None:
        pass

    def _heapify_down(self, index: int = 0) -> None:
        pass

    def insert(self, value: T) -> None:
        pass

    def build_heap(self, arr: List[T]) -> None:
        pass

    def extract_max(self) -> T:
        pass

    def replace(self, value: T) -> T:
        pass

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
        return f"MaxHeap({self.heap})"
