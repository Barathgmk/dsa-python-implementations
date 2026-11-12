"""CircularQueue: Fixed-capacity ring buffer with head/tail indices.

Run this file directly to execute the tests at the bottom.
"""

class CircularQueue:


    def __init__(self, capacity):
        # TODO: set up internal state
        self.capacity = capacity
        self.storage = [None] * capacity
        self.tail = 0
        self.head = 0
        self.size = 0

    def enqueue(self, x):
        """Fail/overwrite when full"""
        if self.is_full():
            raise Exception("Queue is Full")
        self.storage[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        
        self.size +=1

    def dequeue(self):
        if self.is_empty():
            return None
        x = self.storage[self.head] 
        self.head = (self.head + 1) % self.capacity

        self.size -= 1
        return x
    
    def front(self):
        return self.storage[self.head]

    def rear(self):
        return self.storage[(self.tail - 1) % self.capacity]

    def is_full(self):
        if self.size == self.capacity:
            return True
        else:
            return False 

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


def test_circular_queue():
    # Conventions (from your implementation): enqueue on a full queue raises,
    # dequeue on an empty queue returns None.
    q = CircularQueue(3)
    assert q.is_empty() and not q.is_full()
    assert q.dequeue() is None

    q.enqueue(1)
    assert not q.is_empty() and not q.is_full()
    assert q.front() == 1 and q.rear() == 1

    q.enqueue(2)
    q.enqueue(3)
    assert q.is_full() and q.size == 3
    assert q.front() == 1 and q.rear() == 3

    try:
        q.enqueue(4)
        raise AssertionError("enqueue on a full queue should raise")
    except AssertionError:
        raise
    except Exception:
        pass
    assert q.size == 3 and q.front() == 1 and q.rear() == 3  # unchanged

    assert q.dequeue() == 1
    assert not q.is_full() and q.front() == 2

    q.enqueue(4)  # wraps around to index 0
    assert q.is_full() and q.front() == 2 and q.rear() == 4

    assert [q.dequeue(), q.dequeue(), q.dequeue()] == [2, 3, 4]
    assert q.is_empty() and q.dequeue() is None

    # many wrap-arounds with capacity 1 and 2
    one = CircularQueue(1)
    for i in range(10):
        one.enqueue(i)
        assert one.is_full() and one.front() == i and one.rear() == i
        assert one.dequeue() == i and one.is_empty()

    two = CircularQueue(2)
    out = []
    for i in range(20):
        two.enqueue(i)
        if i % 2:
            out += [two.dequeue(), two.dequeue()]
    assert out == list(range(20))


if __name__ == "__main__":
    test_circular_queue()
    print("CircularQueue: all tests passed")
