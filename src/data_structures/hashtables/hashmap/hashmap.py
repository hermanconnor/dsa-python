from typing import TypeVar, Generic, List, Tuple, Optional

K = TypeVar('K')
V = TypeVar('V')


class HashMap(Generic[K, V]):
    def __init__(self, initial_capacity: int = 16) -> None:
        """
        Initialize hash map with given capacity.

        Time Complexity: O(n) where n is initial_capacity
        """
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor = 0.75
        self.buckets: List[List[Tuple[K, V]]] = [[]
                                                 for _ in range(self.capacity)]

    def _hash(self, key: K) -> int:
        """
        Generate hash value for a key.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return hash(key) % self.capacity

    def _resize(self) -> None:
        """
        Double the capacity and rehash all entries.

        Time Complexity: O(n) where n is the number of entries
        """
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        # Rehash all existing entries
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key: K, value: V) -> None:
        """
        Insert or update a key-value pair.

        Time Complexity: O(1) average, O(n) worst case (with resizing)
        """
        # Check if resize is needed
        if self.size / self.capacity >= self.load_factor:
            self._resize()

        idx = self._hash(key)
        bucket = self.buckets[idx]

        # Update existing key
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Add new key-value pair
        bucket.append((key, value))
        self.size += 1

    def get(self, key: K) -> V:
        """
        Retrieve value for a given key.

        Time Complexity: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    def keys(self) -> List[K]:
        """
        Return all keys.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = []

        for bucket in self.buckets:
            for k, v in bucket:
                result.append(k)

        return result

    def values(self) -> List[V]:
        """
        Return all values.

        Time Complexity: O(n)
        """
        result = []

        for bucket in self.buckets:
            for k, v in bucket:
                result.append(v)

        return result

    def items(self) -> List[Tuple[K, V]]:
        """
        Return all key-value pairs.

        Time Complexity: O(n)
        """
        result = []

        for bucket in self.buckets:
            for k, v in bucket:
                result.append((k, v))

        return result

    def remove(self, key: K) -> V:
        """
        Remove a key-value pair.

        Time Complexity: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return v

        raise KeyError(f"Key '{key}' not found")

    def contains(self, key: K) -> bool:
        """
        Check if key exists in hash map.

        Time Complexity: O(1) average, O(n) worst case
        """
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __len__(self) -> int:
        """
        Return number of key-value pairs.

        Time Complexity: O(1)
        """
        return self.size

    def __str__(self) -> str:
        """
        String representation.

        Time Complexity: O(n)
        """
        items = self.items()
        return "{" + ", ".join(f"'{k}': {v}" for k, v in items) + "}"

    def __repr__(self) -> str:
        """
        Official string representation for debugging.

        Time Complexity: O(n)
        """
        items = self.items()
        items_str = ", ".join(f"{k!r}: {v!r}" for k, v in items)
        return f"HashMap({{{items_str}}}, size={self.size}, capacity={self.capacity})"
