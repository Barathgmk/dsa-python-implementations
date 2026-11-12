"""QuadTree: 2D spatial partition.

Conventions (the tests rely on these):
  bounds/rects are (xmin, ymin, xmax, ymax), inclusive; insert returns False if outside bounds.

Run this file directly to execute the tests at the bottom.
"""
import random


class QuadTree:
    def __init__(self, bounds, capacity=4):
        # TODO: set up internal state
        raise NotImplementedError

    def insert(self, point):
        """insert"""
        raise NotImplementedError

    def query_range(self, rect):
        """query_range"""
        raise NotImplementedError

    def _subdivide(self):
        """_subdivide"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_quadtree():

    rng = random.Random(13)
    qt = QuadTree((0, 0, 100, 100), capacity=4)
    pts = list({(rng.randint(0, 100), rng.randint(0, 100)) for _ in range(500)})
    for p in pts:
        assert qt.insert(p)
    assert not qt.insert((200, 200)) and not qt.insert((-1, 5))
    for _ in range(50):
        x1, y1 = rng.randint(0, 80), rng.randint(0, 80)
        rect = (x1, y1, x1 + rng.randint(0, 40), y1 + rng.randint(0, 40))
        want = sorted(p for p in pts if rect[0] <= p[0] <= rect[2] and rect[1] <= p[1] <= rect[3])
        assert sorted(qt.query_range(rect)) == want, rect
    assert sorted(qt.query_range((0, 0, 100, 100))) == sorted(pts)


if __name__ == "__main__":
    test_quadtree()
    print("QuadTree: all tests passed")
