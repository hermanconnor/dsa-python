import pytest
from src.data_structures.my_deque.deque import Node, Deque


@pytest.fixture
def empty_deque():
    """Returns an empty Deque instance."""
    return Deque()


@pytest.fixture
def populated_deque():
    """Return a deque pre-populated with sample integers."""
    dq = Deque()
