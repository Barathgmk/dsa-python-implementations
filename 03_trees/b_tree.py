"""BTree: B-Tree of minimum degree t (database indexing). Later try B+ tree.

Run this file directly to execute the tests at the bottom.
"""
import random


class BTree:
    def __init__(self, t=2):
        # TODO: set up internal state
        raise NotImplementedError

    def insert(self, k):
        """insert"""
        raise NotImplementedError

    def search(self, k):
        """search"""
        raise NotImplementedError

    def delete(self, k):
        """delete"""
        raise NotImplementedError

    def _split_child(self, parent, i):
        """_split_child"""
        raise NotImplementedError

    def keys(self):
        """Sorted list of all keys"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_b_tree():

    for t_deg in (2, 3, 5):
        rng = random.Random(t_deg)
        bt = BTree(t_deg)
        vals = rng.sample(range(5000), 1000)
        for v in vals:
            bt.insert(v)
        assert bt.keys() == sorted(vals)
        assert all(bt.search(v) for v in vals[:100]) and not bt.search(-1)
        bt.insert(vals[0])  # duplicate ignored
        assert bt.keys() == sorted(vals)
        gone = vals[::2]
        for v in gone:
            assert bt.delete(v)
        assert not bt.delete(-1)
        rest = sorted(set(vals) - set(gone))
        assert bt.keys() == rest and not bt.search(gone[0]) and bt.search(rest[0])


if __name__ == "__main__":
    test_b_tree()
    print("BTree: all tests passed")
