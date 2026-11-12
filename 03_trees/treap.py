"""Treap: BST by key + heap by random priority.

Run this file directly to execute the tests at the bottom.
"""
import random


class Treap:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def insert(self, key):
        """insert"""
        raise NotImplementedError

    def delete(self, key):
        """delete"""
        raise NotImplementedError

    def search(self, key):
        """search"""
        raise NotImplementedError

    def _split(self, node, key):
        """_split"""
        raise NotImplementedError

    def _merge(self, a, b):
        """_merge"""
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


def test_treap():

    t = Treap()
    for i in range(1, 1001):
        t.insert(i)
    assert t.inorder() == list(range(1, 1001)) and len(t) == 1000
    assert t.height() <= 60, f"not balanced: height {t.height()}"
    for i in range(1, 1001, 2):
        assert t.delete(i)
    assert t.inorder() == list(range(2, 1001, 2))
    assert t.search(500) and not t.search(501)
    rng = random.Random(3)
    ref, t = set(), Treap()
    for _ in range(1000):
        x = rng.randint(0, 200)
        if rng.random() < 0.6:
            t.insert(x); ref.add(x)
        else:
            t.delete(x); ref.discard(x)
    assert t.inorder() == sorted(ref)


if __name__ == "__main__":
    test_treap()
    print("Treap: all tests passed")
