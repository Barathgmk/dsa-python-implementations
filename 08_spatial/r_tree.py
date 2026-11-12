"""RTree: Bounding-rectangle tree for geospatial data.

Conventions (the tests rely on these):
  Rects are (xmin, ymin, xmax, ymax); search returns all rects intersecting the query (touching counts).

Run this file directly to execute the tests at the bottom.
"""
import random


class RTree:
    def __init__(self, max_entries=4):
        # TODO: set up internal state
        raise NotImplementedError

    def insert(self, rect):
        """insert"""
        raise NotImplementedError

    def search(self, rect):
        """search"""
        raise NotImplementedError

    def _split_node(self, node):
        """_split_node"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_r_tree():

    rng = random.Random(15)
    def hit(a, b): return a[0] <= b[2] and b[0] <= a[2] and a[1] <= b[3] and b[1] <= a[3]
    rt, rects = RTree(), []
    for _ in range(300):
        x, y = rng.randint(0, 100), rng.randint(0, 100)
        r = (x, y, x + rng.randint(0, 10), y + rng.randint(0, 10))
        rects.append(r); rt.insert(r)
    for _ in range(50):
        x, y = rng.randint(0, 100), rng.randint(0, 100)
        q = (x, y, x + rng.randint(0, 25), y + rng.randint(0, 25))
        assert sorted(rt.search(q)) == sorted(r for r in rects if hit(r, q)), q
    assert rt.search((500, 500, 600, 600)) == []


if __name__ == "__main__":
    test_r_tree()
    print("RTree: all tests passed")
