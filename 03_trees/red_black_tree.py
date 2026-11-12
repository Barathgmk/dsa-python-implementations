"""RedBlackTree: Self-balancing BST via node colors.

Run this file directly to execute the tests at the bottom.
"""
import random


class RedBlackTree:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def insert(self, x):
        """insert"""
        raise NotImplementedError

    def delete(self, x):
        """delete"""
        raise NotImplementedError

    def search(self, x):
        """search"""
        raise NotImplementedError

    def _fix_insert(self, node):
        """_fix_insert"""
        raise NotImplementedError

    def _fix_delete(self, node):
        """_fix_delete"""
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


def test_red_black_tree():

    t = RedBlackTree()
    for i in range(1, 1001):
        t.insert(i)
    assert t.inorder() == list(range(1, 1001)) and len(t) == 1000
    assert t.height() <= 2 * 10, f"not balanced: height {t.height()}"  # <= 2*log2(n+1)
    for i in range(1, 1001, 2):
        assert t.delete(i)
    assert t.inorder() == list(range(2, 1001, 2)) and t.height() <= 2 * 10
    assert t.search(500) and not t.search(501)
    rng = random.Random(2)
    ref, t = set(), RedBlackTree()
    for _ in range(1000):
        x = rng.randint(0, 200)
        if rng.random() < 0.6:
            t.insert(x); ref.add(x)
        else:
            t.delete(x); ref.discard(x)
    assert t.inorder() == sorted(ref)


if __name__ == "__main__":
    test_red_black_tree()
    print("RedBlackTree: all tests passed")
