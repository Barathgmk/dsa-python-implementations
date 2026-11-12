"""IntervalTree: Augmented BST storing max endpoint; finds overlapping intervals.

Conventions (the tests rely on these):
  Intervals are closed; query_overlaps returns a list of (lo, hi) tuples.

Run this file directly to execute the tests at the bottom.
"""
import random


class IntervalTree:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def insert(self, lo, hi):
        """insert"""
        raise NotImplementedError

    def delete(self, lo, hi):
        """delete"""
        raise NotImplementedError

    def query_overlaps(self, lo, hi):
        """query_overlaps"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_interval_tree():

    def brute(ivs, lo, hi):
        return sorted(iv for iv in ivs if iv[0] <= hi and lo <= iv[1])
    t = IntervalTree()
    ivs = [(15, 20), (10, 30), (17, 19), (5, 20), (12, 15), (30, 40)]
    for lo, hi in ivs:
        t.insert(lo, hi)
    assert sorted(t.query_overlaps(14, 16)) == brute(ivs, 14, 16)
    assert sorted(t.query_overlaps(40, 50)) == [(30, 40)]  # closed intervals touch
    assert t.query_overlaps(41, 50) == []
    assert t.delete(10, 30)
    ivs.remove((10, 30))
    assert sorted(t.query_overlaps(21, 29)) == brute(ivs, 21, 29) == []
    rng = random.Random(5)
    ivs, t = [], IntervalTree()
    for _ in range(200):
        lo = rng.randint(0, 100); hi = lo + rng.randint(0, 20)
        ivs.append((lo, hi)); t.insert(lo, hi)
    for _ in range(100):
        lo = rng.randint(0, 120); hi = lo + rng.randint(0, 15)
        assert sorted(t.query_overlaps(lo, hi)) == brute(ivs, lo, hi)


if __name__ == "__main__":
    test_interval_tree()
    print("IntervalTree: all tests passed")
