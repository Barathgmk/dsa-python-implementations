"""FenwickTree: Binary indexed tree: prefix sums with updates.

Conventions (the tests rely on these):
  0-based indices; prefix_sum(i) includes i; range_sum is inclusive.

Run this file directly to execute the tests at the bottom.
"""
import random


class FenwickTree:
    def __init__(self, n):
        # TODO: set up internal state
        raise NotImplementedError

    def update(self, i, delta):
        """update"""
        raise NotImplementedError

    def prefix_sum(self, i):
        """prefix_sum"""
        raise NotImplementedError

    def range_sum(self, l, r):
        """range_sum"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_fenwick_tree():

    rng = random.Random(11)
    n = 64
    fw, ref = FenwickTree(n), [0] * n
    for _ in range(500):
        if rng.random() < 0.5:
            i = rng.randrange(n); d = rng.randint(-20, 20)
            ref[i] += d; fw.update(i, d)
        else:
            l = rng.randrange(n); r = rng.randrange(l, n)
            assert fw.prefix_sum(r) == sum(ref[:r + 1])
            assert fw.range_sum(l, r) == sum(ref[l:r + 1])
    fw = FenwickTree(5)
    fw.update(0, 3); fw.update(4, 7)
    assert fw.prefix_sum(0) == 3 and fw.prefix_sum(3) == 3 and fw.prefix_sum(4) == 10


if __name__ == "__main__":
    test_fenwick_tree()
    print("FenwickTree: all tests passed")
