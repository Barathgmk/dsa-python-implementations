"""MinHeap: Binary heap in an array. Parametrize for max-heap / key function.

Run this file directly to execute the tests at the bottom.
"""
import random


class MinHeap:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def push(self, x):
        """push"""
        raise NotImplementedError

    def pop(self):
        """pop"""
        raise NotImplementedError

    def peek(self):
        """peek"""
        raise NotImplementedError

    def heapify(self, arr):
        """O(n) build"""
        raise NotImplementedError

    def _sift_up(self, i):
        """_sift_up"""
        raise NotImplementedError

    def _sift_down(self, i):
        """_sift_down"""
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


def test_heap():

    rng = random.Random(6)
    h = MinHeap()
    assert len(h) == 0
    _raises(IndexError, h.pop)
    _raises(IndexError, h.peek)
    vals = [rng.randint(0, 1000) for _ in range(500)]
    for v in vals:
        h.push(v)
        assert h.peek() == min(h.peek(), v)
    assert len(h) == 500 and h.peek() == min(vals)
    assert [h.pop() for _ in range(500)] == sorted(vals)
    h.heapify([5, 3, 8, 1, 9, 2])
    assert len(h) == 6 and h.peek() == 1
    assert [h.pop() for _ in range(6)] == [1, 2, 3, 5, 8, 9]


if __name__ == "__main__":
    test_heap()
    print("MinHeap: all tests passed")
