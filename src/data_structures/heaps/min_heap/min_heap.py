from typing import Generic, TypeVar, Optional, List, Callable

T = TypeVar('T')


class MinHeap(Generic[T]):
    def __init__(self, key: Optional[Callable[[T], any]] = None) -> None:
        """
        Initialize an empty min heap with optional key function.

        Args:
            key: Optional function to extract comparison key from elements.
                 If None, elements are compared directly.

        Time complexity: O(1)
        """
        self.heap: List[T] = []
        self.key: Callable[[T], any] = key if key else lambda x: x

    def parent(self):
        pass

    def left_child(self):
        pass

    def right_child(self):
        pass

    def has_parent(self):
        pass

    def has_left_child(self):
        pass

    def has_right_child(self):
        pass

    def swap(self):
        pass

    def insert(self):
        pass

    def heapify_up(self):
        pass

    def heapify_down(self):
        pass

    def build_heap(self):
        pass

    def extract_min(self):
        pass

    def __len__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
