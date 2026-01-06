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

    def find(self, x: int) -> int:
        """
        Find the root of the set containing x with path compression.
        Time complexity: O(α(n)) where α is inverse Ackermann function
        """
        if not (0 <= x < self._n):
            raise IndexError(f"Index {x} is out of bounds [0, {self._n-1}]")

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union the sets containing x and y using union by rank.
        Returns True if union was performed, False if already connected.
        Time complexity: O(α(n))
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

         # Union by rank: attach smaller rank tree under larger rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self._components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """
        Check if x and y are in the same connected component.
        Time complexity: O(α(n))
        """
        return self.find(x) == self.find(y)

    @property
    def components(self) -> int:
        """Return the number of connected components."""
        return self._components

    def component_size(self, x: int) -> int:
        """
        Return the size of the component containing x.
        Time complexity: O(α(n))
        """
        root = self.find(x)

        return sum(1 for i in range(self._n) if self.find(i) == root)

    def get_all_components(self) -> dict[int, list[int]]:
        """
        Return a dictionary mapping each root to its component members.
        Time complexity: O(n * α(n))
        """
        components: dict[int, list[int]] = {}

        for i in range(self._n):
            root = self.find(i)
            components.setdefault(root, []).append(i)

        return components

    def __len__(self) -> int:
        """Return the total number of elements."""
        return self._n

    def __str__(self) -> str:
        """
        Return a human-readable string representation.
        """
        components = self.get_all_components()
        component_list = [f"Set {root}: {members}"
                          for root, members in components.items()]

        return (f"UnionFind with {self.components} component(s):\n"
                f"{'; '.join(component_list)}")

    def __repr__(self) -> str:
        """
        Return a detailed string representation for debugging.
        """
        if len(self.rank) != self._n:
            return f"UnionFind(n={self._n}, state=INVALID)"

        return (f"UnionFind(n={self._n}, components={self.components}, "
                f"parent={self.parent}, rank={self.rank})")
