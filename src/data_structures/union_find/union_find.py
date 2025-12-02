class UnionFind:
    def __init__(self, n: int):
        """
        Initialize Union Find with n elements (0 to n-1).
        Each element starts as its own parent (disjoint sets).
        """
        if n < 0:
            raise ValueError("n must be non-negative")

        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [0] * n
        self._components: int = n
        self._n: int = n  # Cache size for O(1) access

    def find(self):
        pass

    def union(self):
        pass

    def __len__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
