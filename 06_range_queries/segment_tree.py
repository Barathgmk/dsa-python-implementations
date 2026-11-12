"""SegmentTree: Range sum/min queries with point + range updates (lazy propagation).

Conventions (the tests rely on these):
  Sum tree. Indices are 0-based and ranges inclusive. update sets a value; range_update ADDS v to each element.

Run this file directly to execute the tests at the bottom.
"""
import random


class SegmentTree:
    def __init__(self, arr):
        # TODO: set up internal state
        raise NotImplementedError

    def build(self, arr):
        """build"""
        raise NotImplementedError

    def query(self, l, r):
        """query"""
        raise NotImplementedError

    def update(self, i, v):
        """update"""
        raise NotImplementedError

    def range_update(self, l, r, v):
        """Lazy"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_segment_tree():

    rng = random.Random(10)
    arr = [rng.randint(-50, 50) for _ in range(50)]
    st = SegmentTree(arr)
    for _ in range(500):
        r = rng.random()
        if r < 0.4:
            i = rng.randrange(50); v = rng.randint(-50, 50)
            arr[i] = v; st.update(i, v)
        elif r < 0.6:
            l = rng.randrange(50); rr = rng.randrange(l, 50); v = rng.randint(-10, 10)
            for j in range(l, rr + 1):
                arr[j] += v
            st.range_update(l, rr, v)
        else:
            l = rng.randrange(50); rr = rng.randrange(l, 50)
            assert st.query(l, rr) == sum(arr[l:rr + 1]), (l, rr)
    assert st.query(0, 49) == sum(arr) and st.query(7, 7) == arr[7]


if __name__ == "__main__":
    test_segment_tree()
    print("SegmentTree: all tests passed")
