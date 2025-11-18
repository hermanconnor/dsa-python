from __future__ import annotations
from collections import defaultdict, deque
from typing import (
    Any, Dict, List, Optional, Set, Tuple,
    TypeVar, Hashable, Generic, Deque
)

V = TypeVar('V', bound=Hashable)
W = TypeVar('W', bound=Any)


class UndirectedGraph(Generic[V, W]):
    """
    An undirected graph implementation with optional edge weights.
    Uses adjacency list representation for efficiency.
    """

    def __init__(self) -> None:
        """
        Initialize an empty undirected graph.

        Time Complexity: O(1)
        """
        self.graph: Dict[V, List[Tuple[V, W]]] = defaultdict(list)

    def add_vertex(self, vertex: V) -> None:
        pass
