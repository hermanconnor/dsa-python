import pytest
from src.data_structures.stack.stack import Stack


@pytest.fixture
def empty_stack():
    """Returns an empty Stack instance."""
    return Stack()


@pytest.fixture
def populated_stack():
    """Returns a Stack instance with 'a', 'b', 'c'."""
    stack = Stack()

    stack.push("a")
    stack.push("b")
    stack.push("c")

    return stack


def test_new_stack_is_empty(empty_stack):
    """Test that a newly created stack is empty."""
    assert empty_stack.is_empty()
    assert len(empty_stack) == 0


def test_push_adds_item(empty_stack):
    """Test that push adds an item and changes stack state."""
    empty_stack.push(1)

    assert not empty_stack.is_empty()
    assert len(empty_stack) == 1
    assert empty_stack.peek() == 1


def test_push_multiple_items(empty_stack):
    """Test pushing multiple items maintains order."""
    empty_stack.push('first')
    empty_stack.push('second')

    assert len(empty_stack) == 2
    assert empty_stack.peek() == 'second'


def test_pop_removes_and_returns_top_item(populated_stack):
    """Test pop removes the top item and returns its value."""
    top_item = populated_stack.pop()

    assert top_item == 'c'
    assert len(populated_stack) == 2
    assert populated_stack.peek() == 'b'


def test_pop_raises_indexerror_on_empty_stack(empty_stack):
    """Test pop raises IndexError when called on an empty stack."""
    with pytest.raises(IndexError) as e:
        empty_stack.pop()

    assert "pop from empty stack" in str(e.value)


def test_peek_returns_top_item_without_removal(populated_stack):
    """Test peek returns the top item without changing the stack size."""
    size_before = len(populated_stack)
    top_item = populated_stack.peek()
    size_after = len(populated_stack)

    assert top_item == 'c'
    assert size_before == size_after


def test_peek_raises_indexerror_on_empty_stack(empty_stack):
    """Test peek raises IndexError when called on an empty stack."""
    with pytest.raises(IndexError) as e:
        empty_stack.peek()

    assert "peek from empty stack" in str(e.value)


def test_is_empty_true(empty_stack):
    """Test is_empty returns True for an empty stack."""
    assert empty_stack.is_empty()


def test_is_empty_false(populated_stack):
    """Test is_empty returns False for a non-empty stack."""
    assert not populated_stack.is_empty()


def test_clear_makes_stack_empty(populated_stack):
    """Test clear removes all items."""
    populated_stack.clear()

    assert populated_stack.is_empty()
    assert len(populated_stack) == 0


def test_clear_on_empty_stack_remains_empty(empty_stack):
    """Test calling clear on an already empty stack."""
    empty_stack.clear()

    assert empty_stack.is_empty()


def test_len_returns_correct_size(populated_stack):
    """Test __len__ returns the correct number of items."""
    assert len(populated_stack) == 3


def test_len_returns_zero_for_empty_stack(empty_stack):
    """Test __len__ returns 0 for an empty stack."""
    assert len(empty_stack) == 0


def test_str_representation(populated_stack):
    """Test __str__ provides the user-friendly representation (top first)."""
    # Items are ['a', 'b', 'c']. Stack representation is Top -> ['c', 'b', 'a']
    assert str(populated_stack) == "Top -> ['c', 'b', 'a']"


def test_repr_representation(populated_stack):
    """Test __repr__ provides the detailed representation."""
    # Items are ['a', 'b', 'c']. Internal list is used for repr.
    assert repr(populated_stack) == "Stack(['a', 'b', 'c'])"


def test_repr_empty_stack(empty_stack):
    """Test __repr__ for an empty stack."""
    assert repr(empty_stack) == "Stack([])"
