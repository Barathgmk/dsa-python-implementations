"""UnionFind: Disjoint set union with path compression + union by rank.

Conventions (the tests rely on these):
  union returns True if it merged two different sets.

Run this file directly to execute the tests at the bottom.
"""


class UnionFind:
    def __init__(self, n):
        # TODO: set up internal state
        raise NotImplementedError

    def find(self, x):
        """find"""
        raise NotImplementedError

    def union(self, a, b):
        """union"""
        raise NotImplementedError

    def connected(self, a, b):
        """connected"""
        raise NotImplementedError

    def count(self):
        """Number of components"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_union_find():

    uf = UnionFind(10)
    assert uf.count() == 10 and not uf.connected(0, 1)
    assert uf.union(0, 1) and not uf.union(1, 0)
    assert uf.connected(0, 1) and uf.count() == 9
    uf.union(2, 3); uf.union(1, 3)
    assert uf.connected(0, 2) and uf.count() == 7
    assert uf.find(0) == uf.find(3) and uf.find(0) != uf.find(9)
    for i in range(9):
        uf.union(i, i + 1)  # long chain
    assert uf.count() == 1 and all(uf.connected(0, i) for i in range(10))


if __name__ == "__main__":
    test_union_find()
    print("UnionFind: all tests passed")
