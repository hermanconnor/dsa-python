from typing import List, Optional, Any, TypeVar, Generic

T = TypeVar('T')


class CircularQueue(Generic[T]):
    def __init__(self, capacity: int) -> None:
        """
        Initialize circular queue with given capacity.

        Time Complexity: O(n) where n is capacity (due to list initialization)
        Space Complexity: O(n)
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        self.capacity: int = capacity
        self.queue: List[Optional[T]] = [None] * capacity
        self.front: int = 0
        self.size: int = 0

    def is_empty(self) -> bool:
        """Check if queue is empty. Time Complexity: O(1)"""
        return self.size == 0

    def is_full(self) -> bool:
        """Check if queue is full. Time Complexity: O(1)"""
        return self.size == self.capacity

    def enqueue(self, item: T) -> bool:
        """Add item to the rear of the queue.Time Complexity: O(1)"""
        if self.is_full():
            raise IndexError("Queue is full (capacity reached)")

        # Calculate the index where the new element goes (the rear)
        # Rear index is (front + size) % capacity
        rear_index = (self.front + self.size) % self.capacity
        self.queue[rear_index] = item
        self.size += 1
        return True

    def dequeue(self) -> T:
        """Remove and return item from front of queue.Time Complexity: O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.queue[self.front]

        # Set the old slot to None for proper garbage collection
        self.queue[self.front] = None

        # Move front index circularly
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return item

    def peek(self) -> T:
        """Return front item without removing it.Time Complexity: O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.queue[self.front]

    def __len__(self) -> int:
        """Return the current size of the queue. Time Complexity: O(1)"""
        return self.size

    def __str__(self) -> str:
        """
        String representation of queue. Shows elements from front to rear.

        Time Complexity: O(n) where n is the number of elements
        """
        if self.is_empty():
            return "[]"

        elements = []
        i = self.front
        for _ in range(self.size):
            elements.append(str(self.queue[i]))
            i = (i + 1) % self.capacity

        return "[" + " <- ".join(elements) + "]"

    def __repr__(self) -> str:
        """
        Developer-friendly representation of the circular queue.
        """
        return (f"CircularQueue[T](capacity={self.capacity}, size={self.size}, "
                f"front_index={self.front})")
