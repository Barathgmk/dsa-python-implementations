"""BST: Binary search tree.

Conventions (the tests rely on these):
  Duplicates ignored; delete/search return bool; min/max return None when empty; kth_smallest is 1-indexed, IndexError if out of range.

Run this file directly to execute the tests at the bottom.
"""
import random


class BST:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def insert(self, x):
        """insert"""
        raise NotImplementedError

    def search(self, x):
        """search"""
        raise NotImplementedError

    def delete(self, x):
        """delete"""
        raise NotImplementedError

    def min(self):
        """min"""
        raise NotImplementedError

    def max(self):
        """max"""
        raise NotImplementedError

    def is_valid(self):
        """Validate BST property"""
        raise NotImplementedError

    def kth_smallest(self, k):
        """kth_smallest"""
        raise NotImplementedError

    def inorder(self):
        """Sorted list of keys"""
        raise NotImplementedError

    def height(self):
        """Nodes on longest root-leaf path; empty = 0"""
        raise NotImplementedError

    def __len__(self):
        """__len__"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_bst():

    t = BST()
    assert len(t) == 0 and t.min() is None and t.max() is None and not t.search(1)
    for x in (5, 3, 8, 1, 4, 7, 9):
        t.insert(x)
    t.insert(5)  # duplicate
    assert len(t) == 7 and t.inorder() == [1, 3, 4, 5, 7, 8, 9]
    assert t.search(4) and not t.search(6)
    assert t.min() == 1 and t.max() == 9 and t.is_valid()
    assert t.kth_smallest(1) == 1 and t.kth_smallest(4) == 5 and t.kth_smallest(7) == 9
    _raises(IndexError, t.kth_smallest, 8)
    assert t.delete(1)            # leaf
    assert t.delete(3)            # one child
    assert t.delete(5)            # two children (root)
    assert not t.delete(100)
    assert t.inorder() == [4, 7, 8, 9] and t.is_valid() and len(t) == 4
    rng = random.Random(0)
    ref, t = set(), BST()
    for _ in range(500):
        x = rng.randint(0, 100)
        if rng.random() < 0.6:
            t.insert(x); ref.add(x)
        else:
            assert bool(t.delete(x)) == (x in ref); ref.discard(x)
        assert t.inorder() == sorted(ref)
    assert t.is_valid()


if __name__ == "__main__":
    test_bst()
    print("BST: all tests passed")
