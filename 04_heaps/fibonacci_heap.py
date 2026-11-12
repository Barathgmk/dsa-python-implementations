"""FibonacciHeap: Amortized O(1) insert/decrease-key. Advanced.

Conventions (the tests rely on these):
  insert returns a node handle; find_min/extract_min return keys.

Run this file directly to execute the tests at the bottom.
"""
import random


class FibonacciHeap:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def insert(self, key):
        """insert"""
        raise NotImplementedError

    def find_min(self):
        """find_min"""
        raise NotImplementedError

    def extract_min(self):
        """extract_min"""
        raise NotImplementedError

    def decrease_key(self, node, key):
        """decrease_key"""
        raise NotImplementedError

    def merge(self, other):
        """merge"""
        raise NotImplementedError

    def _consolidate(self):
        """_consolidate"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_fibonacci_heap():

    rng = random.Random(7)
    fh = FibonacciHeap()
    assert len(fh) == 0
    vals = [rng.randint(0, 1000) for _ in range(300)]
    for v in vals:
        fh.insert(v)
    assert len(fh) == 300 and fh.find_min() == min(vals)
    assert [fh.extract_min() for _ in range(300)] == sorted(vals)
    fh = FibonacciHeap()
    nodes = {k: fh.insert(k) for k in (10, 20, 30, 40, 50)}
    fh.extract_min()  # forces consolidation
    fh.decrease_key(nodes[50], 1)
    assert fh.find_min() == 1
    assert fh.extract_min() == 1 and fh.extract_min() == 20
    a, b = FibonacciHeap(), FibonacciHeap()
    for v in (5, 7, 9): a.insert(v)
    for v in (1, 6, 8): b.insert(v)
    a.merge(b)
    assert len(a) == 6 and [a.extract_min() for _ in range(6)] == [1, 5, 6, 7, 8, 9]


if __name__ == "__main__":
    test_fibonacci_heap()
    print("FibonacciHeap: all tests passed")
