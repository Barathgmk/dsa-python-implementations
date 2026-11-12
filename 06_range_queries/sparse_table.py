"""SparseTable: Static range min/max in O(1) after O(n log n) build.

Conventions (the tests rely on these):
  Range MIN, inclusive bounds.

Run this file directly to execute the tests at the bottom.
"""
import random


class SparseTable:
    def __init__(self, arr):
        # TODO: set up internal state
        raise NotImplementedError

    def build(self, arr):
        """build"""
        raise NotImplementedError

    def query(self, l, r):
        """query"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_sparse_table():

    rng = random.Random(12)
    arr = [rng.randint(-100, 100) for _ in range(37)]
    st = SparseTable(arr)
    for l in range(len(arr)):
        for r in range(l, len(arr)):
            assert st.query(l, r) == min(arr[l:r + 1]), (l, r)
    assert SparseTable([42]).query(0, 0) == 42


if __name__ == "__main__":
    test_sparse_table()
    print("SparseTable: all tests passed")
