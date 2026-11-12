"""KDTree: k-d tree for nearest neighbor search.

Conventions (the tests rely on these):
  Points are tuples; nearest returns a point; range_search(lo, hi) returns points in the box, inclusive.

Run this file directly to execute the tests at the bottom.
"""
import random


class KDTree:
    def __init__(self, k=2):
        # TODO: set up internal state
        raise NotImplementedError

    def build(self, points):
        """build"""
        raise NotImplementedError

    def insert(self, point):
        """insert"""
        raise NotImplementedError

    def nearest(self, target):
        """nearest"""
        raise NotImplementedError

    def range_search(self, lo, hi):
        """range_search"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_kd_tree():

    rng = random.Random(14)
    pts = [(rng.random() * 100, rng.random() * 100) for _ in range(300)]
    kd = KDTree()
    kd.build(pts)
    def d2(a, b): return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    for _ in range(50):
        q = (rng.random() * 100, rng.random() * 100)
        assert kd.nearest(q) == min(pts, key=lambda p: d2(p, q))
    extra = (50.5, 50.5)
    kd.insert(extra)
    assert kd.nearest((50.5, 50.6)) == extra
    pts.append(extra)
    for _ in range(30):
        lo = (rng.random() * 60, rng.random() * 60)
        hi = (lo[0] + rng.random() * 40, lo[1] + rng.random() * 40)
        want = sorted(p for p in pts if lo[0] <= p[0] <= hi[0] and lo[1] <= p[1] <= hi[1])
        assert sorted(kd.range_search(lo, hi)) == want


if __name__ == "__main__":
    test_kd_tree()
    print("KDTree: all tests passed")
