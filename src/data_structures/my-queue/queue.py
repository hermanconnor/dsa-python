class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self._next = None


class Queue:
    """Implements a Queue using a linked list."""

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data) -> None:
        """Add an element to the rear of the queue - O(1)"""
        new_node = Node(data)

        if self.rear is None:
            # Queue is empty, the new node is both front and rear
            self.front = new_node
            self.rear = new_node
        else:
            # Link the current rear's _next to the new node, then update rear
            self.rear._next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self):
        """Remove and return element from the front of the queue - O(1)"""
        if self.front is None:
            raise IndexError("dequeue from empty queue")

        # 1. Store data and advance the front pointer
        data = self.front.data
        self.front = self.front._next

        # 2. If advancing front made it None (queue is now empty),
        #    update rear to None also.
        if self.front is None:
            self.rear = None

        self.size -= 1
        return data

    def peek(self):
        """Return the front element without removing it - O(1)"""
        if self.front is None:
            raise IndexError("peek from empty queue")

        return self.front.data

    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return self.front is None

    def __len__(self):
        """Returns the number of elements in the queue."""
        return self.size

    def __str__(self):
        """
        Returns a human-readable string representation of the queue.
        e.g., "Queue: [10, 20, 30] (Front -> Rear)"
        """
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current._next

        return f"Queue: [{', '.join(elements)}] (Front -> Rear)"

    def __repr__(self):
        """
        Returns an official string representation.
        """
        return f"Queue(size={self.size}, front={self.front.data if self.front else None})"
