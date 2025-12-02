from typing import TypeVar, Generic, List, Iterator

T = TypeVar('T')


class HashSet(Generic[T]):
    def __init__(self, initial_capacity: int = 16) -> None:
        """
        Initialize hash set with given capacity.

        Time Complexity: O(n) where n is initial_capacity
        """
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor = 0.75
        self.buckets: List[List[T]] = [[] for _ in range(self.capacity)]

    def _hash(self, element: T) -> int:
        """
        Generate hash value for an element.

        Time Complexity: O(1)
        """
        return hash(element) % self.capacity

    def _resize(self) -> None:
        """
        Double the capacity and rehash all elements.

        Time Complexity: O(n) where n is the number of elements
        """
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for element in bucket:
                self.add(element)

    def add(self, element: T) -> bool:
        """
        Add an element to the set.

        Returns True if element was added, False if already present.

        Time Complexity: O(1) average, O(n) worst case (with resizing)
        """
        if self.size / self.capacity >= self.load_factor:
            self._resize()

        index = self._hash(element)
        bucket = self.buckets[index]

        # Check if element already exists
        if element in bucket:
            return False

        # Add new element
        bucket.append(element)
        self.size += 1
        return True

    def remove(self, element: T) -> bool:
        """
        Remove an element from the set.

        Returns True if element was removed, False if not found.

        Time Complexity: O(1) average, O(n) worst case
        """
        index = self._hash(element)
        bucket = self.buckets[index]

        try:
            bucket.remove(element)
            self.size -= 1
            return True
        except ValueError:
            return False

    def clear(self) -> None:
        """
        Remove all elements from the set.

        Time Complexity: O(n)
        """
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

    def union(self, other: 'HashSet[T]') -> 'HashSet[T]':
        """
        Return a new set with elements from both sets.

        Time Complexity: O(n + m) where n and m are sizes of the sets
        """
        result = HashSet[T](max(self.capacity, other.capacity))

        for element in self:
            result.add(element)

        for element in other:
            result.add(element)

        return result

    def intersection(self, other: 'HashSet[T]') -> 'HashSet[T]':
        """
        Return a new set with elements common to both sets.

        Time Complexity: O(min(n, m))
        """
        result = HashSet[T]()

        # Iterate through smaller set for efficiency
        smaller, larger = (self, other) if len(
            self) <= len(other) else (other, self)

        for element in smaller:
            if larger.contains(element):
                result.add(element)

        return result

    def difference(self, other: 'HashSet[T]') -> 'HashSet[T]':
        """
        Return a new set with elements in this set but not in other.

        Time Complexity: O(n)
        """
        result = HashSet[T]()

        for element in self:
            if not other.contains(element):
                result.add(element)

        return result

    def is_subset(self, other: 'HashSet[T]') -> bool:
        """
        Check if this set is a subset of other.

        Time Complexity: O(n)
        """
        if len(self) > len(other):
            return False

        for element in self:
            if not other.contains(element):
                return False
        return True

    def is_superset(self, other: 'HashSet[T]') -> bool:
        """
        Check if this set is a superset of other.

        Time Complexity: O(m) where m is size of other
        """
        return other.is_subset(self)

    def contains(self, element: T) -> bool:
        """
        Check if element exists in the set.

        Time Complexity: O(1) average, O(n) worst case
        """
        index = self._hash(element)
        bucket = self.buckets[index]

        return element in bucket

    def __len__(self) -> int:
        """
        Return number of elements in the set.

        Time Complexity: O(1)
        """
        return self.size

    def __iter__(self) -> Iterator[T]:
        """
        Make the set iterable.

        Time Complexity: O(n)
        """
        for bucket in self.buckets:
            for element in bucket:
                yield element

    def __contains__(self, element: T) -> bool:
        """
        Support 'in' operator.

        Time Complexity: O(1) average, O(n) worst case
        """
        return self.contains(element)

    def __str__(self) -> str:
        """
        String representation.

        Time Complexity: O(n)
        """
        elements = list(self)
        return "{" + ", ".join(repr(e) for e in elements) + "}"

    def __repr__(self) -> str:
        """
        Official string representation for debugging.

        Time Complexity: O(n)
        """
        elements = list(self)
        elements_str = ", ".join(repr(e) for e in elements)
        return f"HashSet({{{elements_str}}}, size={self.size}, capacity={self.capacity})"
