"""PriorityQueue: Priority queue on your heap, with decrease_key support (for Dijkstra).

Conventions (the tests rely on these):
  pop returns the item with the lowest priority value.

Run this file directly to execute the tests at the bottom.
"""


class PriorityQueue:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def push(self, item, priority):
        """push"""
        raise NotImplementedError

    def pop(self):
        """pop"""
        raise NotImplementedError

    def decrease_key(self, item, priority):
        """decrease_key"""
        raise NotImplementedError

    def __len__(self):
        """__len__"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_priority_queue():

    pq = PriorityQueue()
    pq.push("a", 5); pq.push("b", 3); pq.push("c", 8); pq.push("d", 4)
    assert len(pq) == 4
    pq.decrease_key("c", 1)
    pq.decrease_key("a", 2)
    assert [pq.pop() for _ in range(4)] == ["c", "a", "b", "d"]
    assert len(pq) == 0
    _raises(IndexError, pq.pop)


if __name__ == "__main__":
    test_priority_queue()
    print("PriorityQueue: all tests passed")
