import pytest
from priority_queue import PriorityQueue

class TestPriorityQueueBasics:
    """Test basic priority queue operations."""
    
    def test_init_empty(self):
        """Test initialization of empty queue."""
        pq = PriorityQueue()

        assert len(pq) == 0
        assert pq.is_empty()
        assert not pq
    
    def test_init_with_items(self):
        """Test initialization with items."""
        items = [("task1", 3.0), ("task2", 1.0), ("task3", 2.0)]
        pq = PriorityQueue(items)

        assert len(pq) == 3
        assert not pq.is_empty()
        assert pq.pop() == "task2"  # Lowest priority value
    
    def test_push_single_item(self):
        """Test pushing a single item."""
        pq = PriorityQueue()

        pq.push("item1", 5.0)

        assert len(pq) == 1
        assert "item1" in pq
    
    def test_push_multiple_items(self):
        """Test pushing multiple items."""
        pq = PriorityQueue()

        pq.push("low", 10.0)
        pq.push("high", 1.0)
        pq.push("medium", 5.0)

        assert len(pq) == 3

class TestPriorityQueuePop:
    """Test pop operations."""
    
    def test_pop_order(self):
        """Test that items are popped in priority order."""
        pq = PriorityQueue()

        pq.push("third", 3.0)
        pq.push("first", 1.0)
        pq.push("second", 2.0)
        
        assert pq.pop() == "first"
        assert pq.pop() == "second"
        assert pq.pop() == "third"
    
    def test_pop_empty_queue(self):
        """Test popping from empty queue raises IndexError."""
        pq = PriorityQueue()

        with pytest.raises(IndexError, match="pop from empty priority queue"):
            pq.pop()
    
    def test_pop_reduces_length(self):
        """Test that pop reduces queue length."""
        pq = PriorityQueue([("item1", 1.0), ("item2", 2.0)])

        assert len(pq) == 2
        pq.pop()

        assert len(pq) == 1
        pq.pop()

        assert len(pq) == 0
    
    def test_pop_with_equal_priorities(self):
        """Test that equal priorities maintain insertion order."""
        pq = PriorityQueue()

        pq.push("first", 1.0)
        pq.push("second", 1.0)
        pq.push("third", 1.0)
        
        # Should maintain FIFO order for equal priorities
        assert pq.pop() == "first"
        assert pq.pop() == "second"
        assert pq.pop() == "third"

class TestPriorityQueuePeek:
    """Test peek operations."""
    
    def test_peek_returns_highest_priority(self):
        """Test that peek returns highest priority without removing."""
        pq = PriorityQueue()

        pq.push("low", 10.0)
        pq.push("high", 1.0)
        
        assert pq.peek() == "high"
        assert len(pq) == 2  # Should not remove item
    
    def test_peek_empty_queue(self):
        """Test peeking empty queue raises IndexError."""
        pq = PriorityQueue()

        with pytest.raises(IndexError, match="peek from empty priority queue"):
            pq.peek()
    
    def test_peek_after_operations(self):
        """Test peek after various operations."""
        pq = PriorityQueue()

        pq.push("item1", 5.0)
        pq.push("item2", 3.0)

        assert pq.peek() == "item2"
        
        pq.pop()
        assert pq.peek() == "item1"

class TestPriorityQueueUpdate:
    """Test priority update operations."""
    
    def test_update_priority_existing_item(self):
        """Test updating priority of existing item."""
        pq = PriorityQueue()

        pq.push("item1", 5.0)
        pq.push("item2", 3.0)
        
        # Update item1 to have higher priority
        pq.update_priority("item1", 1.0)
        assert pq.pop() == "item1"
        assert pq.pop() == "item2"
    
    def test_update_priority_new_item(self):
        """Test updating priority of non-existent item adds it."""
        pq = PriorityQueue()

        pq.update_priority("new_item", 5.0)

        assert len(pq) == 1
        assert pq.pop() == "new_item"
    
    def test_push_duplicate_updates_priority(self):
        """Test that pushing duplicate item updates its priority."""
        pq = PriorityQueue()

        pq.push("item", 10.0)
        pq.push("item", 1.0)  # Update priority
        
        assert len(pq) == 1  # Should only have one item
        assert pq.pop() == "item"

class TestPriorityQueueRemove:
    """Test remove operations."""
    
    def test_remove_existing_item(self):
        """Test removing an existing item."""
        pq = PriorityQueue()

        pq.push("item1", 1.0)
        pq.push("item2", 2.0)
        
        pq.remove("item1")

        assert "item1" not in pq
        assert len(pq) == 1
        assert pq.pop() == "item2"
    
    def test_remove_nonexistent_item(self):
        """Test removing non-existent item raises KeyError."""
        pq = PriorityQueue()

        pq.push("item1", 1.0)
        
        with pytest.raises(KeyError):
            pq.remove("nonexistent")
    
    def test_remove_all_items(self):
        """Test removing all items one by one."""
        pq = PriorityQueue()

        pq.push("item1", 1.0)
        pq.push("item2", 2.0)
        pq.push("item3", 3.0)
        
        pq.remove("item1")
        pq.remove("item2")
        pq.remove("item3")
        
        assert pq.is_empty()
        assert len(pq) == 0

class TestPriorityQueueUtilityMethods:
    """Test utility methods."""
    
    def test_is_empty_on_empty_queue(self):
        """Test is_empty returns True for empty queue."""
        pq = PriorityQueue()

        assert pq.is_empty()
    
    def test_is_empty_on_nonempty_queue(self):
        """Test is_empty returns False for non-empty queue."""
        pq = PriorityQueue()

        pq.push("item", 1.0)

        assert not pq.is_empty()
    
    def test_is_empty_after_pop_all(self):
        """Test is_empty after popping all items."""
        pq = PriorityQueue([("item1", 1.0), ("item2", 2.0)])

        pq.pop()
        pq.pop()

        assert pq.is_empty()
    
    def test_clear_empties_queue(self):
        """Test clear removes all items."""
        pq = PriorityQueue([("item1", 1.0), ("item2", 2.0)])

        pq.clear()

        assert len(pq) == 0
        assert pq.is_empty()
    
    def test_clear_allows_reuse(self):
        """Test queue can be reused after clear."""
        pq = PriorityQueue([("item1", 1.0)])

        pq.clear()
        pq.push("new_item", 5.0)

        assert len(pq) == 1
        assert pq.pop() == "new_item"
    
    def test_contains_existing_item(self):
        """Test __contains__ for existing item."""
        pq = PriorityQueue()

        pq.push("item", 1.0)

        assert "item" in pq
    
    def test_contains_nonexistent_item(self):
        """Test __contains__ for non-existent item."""
        pq = PriorityQueue()

        assert "item" not in pq
    
    def test_contains_after_remove(self):
        """Test __contains__ after removing item."""
        pq = PriorityQueue()

        pq.push("item", 1.0)
        pq.remove("item")

        assert "item" not in pq
    
    def test_bool_empty_queue(self):
        """Test __bool__ for empty queue."""
        pq = PriorityQueue()

        assert not pq
    
    def test_bool_nonempty_queue(self):
        """Test __bool__ for non-empty queue."""
        pq = PriorityQueue()

        pq.push("item", 1.0)

        assert pq

class TestPriorityQueueStringMethods:
    """Test string representation methods."""
    
    def test_repr_empty_queue(self):
        """Test __repr__ for empty queue."""
        pq = PriorityQueue()

        assert repr(pq) == "PriorityQueue([])"
    
    def test_repr_with_items(self):
        """Test __repr__ with items."""
        pq = PriorityQueue()

        pq.push("item1", 1.0)
        pq.push("item2", 2.0)
        
        repr_str = repr(pq)

        assert "PriorityQueue" in repr_str
        assert "item1" in repr_str
        assert "item2" in repr_str
    
    def test_str_empty_queue(self):
        """Test __str__ for empty queue."""
        pq = PriorityQueue()

        assert str(pq) == "PriorityQueue(empty)"
    
    def test_str_with_items(self):
        """Test __str__ with items."""
        pq = PriorityQueue()

        pq.push("task", 1.0)
        
        str_repr = str(pq)

        assert "PriorityQueue" in str_repr
        assert "task" in str_repr
        assert "p=1.0" in str_repr

class TestPriorityQueueEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_negative_priorities(self):
        """Test queue works with negative priorities."""
        pq = PriorityQueue()

        pq.push("item1", 5.0)
        pq.push("item2", -5.0)
        pq.push("item3", 0.0)
        
        assert pq.pop() == "item2"  # -5.0 is lowest
        assert pq.pop() == "item3"  # 0.0
        assert pq.pop() == "item1"  # 5.0
    
    def test_float_priorities(self):
        """Test queue works with float priorities."""
        pq = PriorityQueue()

        pq.push("item1", 1.5)
        pq.push("item2", 1.1)
        pq.push("item3", 1.9)
        
        assert pq.pop() == "item2"
    
    def test_very_large_queue(self):
        """Test queue with many items."""
        pq = PriorityQueue()

        n = 1000
        
        # Add items in reverse priority order
        for i in range(n, 0, -1):
            pq.push(f"item{i}", float(i))
        
        assert len(pq) == n
        
        # Should pop in ascending priority order
        for i in range(1, n + 1):
            assert pq.pop() == f"item{i}"
    
    def test_multiple_updates_same_item(self):
        """Test updating same item multiple times."""
        pq = PriorityQueue()

        pq.push("item", 10.0)
        pq.push("item", 5.0)
        pq.push("item", 1.0)
        
        assert len(pq) == 1
        assert pq.pop() == "item"
        assert pq.is_empty()
    
    def test_interleaved_operations(self):
        """Test complex sequence of operations."""
        pq = PriorityQueue()
        
        pq.push("a", 3.0)
        pq.push("b", 1.0)
        assert pq.pop() == "b"
        
        pq.push("c", 2.0)
        pq.update_priority("a", 0.5)
        assert pq.peek() == "a"
        
        pq.remove("c")
        assert len(pq) == 1


class TestPriorityQueueTypeSupport:
    """Test queue with different types."""
    
    def test_string_items(self):
        """Test queue with string items."""
        pq: PriorityQueue[str] = PriorityQueue()

        pq.push("hello", 1.0)
        pq.push("world", 2.0)

        assert pq.pop() == "hello"
    
    def test_integer_items(self):
        """Test queue with integer items."""
        pq: PriorityQueue[int] = PriorityQueue()

        pq.push(100, 3.0)
        pq.push(200, 1.0)

        assert pq.pop() == 200
    
    def test_tuple_items(self):
        """Test queue with tuple items."""
        pq: PriorityQueue[tuple] = PriorityQueue()

        pq.push((1, 2), 5.0)
        pq.push((3, 4), 2.0)

        assert pq.pop() == (3, 4)
    
    def test_custom_object_items(self):
        """Test queue with custom objects."""
        class Task:
            def __init__(self, name: str):
                self.name = name
            
            def __eq__(self, other):
                return isinstance(other, Task) and self.name == other.name
            
            def __hash__(self):
                return hash(self.name)
        
        pq: PriorityQueue[Task] = PriorityQueue()
        task1 = Task("task1")
        task2 = Task("task2")
        
        pq.push(task1, 5.0)
        pq.push(task2, 1.0)
        
        assert pq.pop() == task2
        assert pq.pop() == task1