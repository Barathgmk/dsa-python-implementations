"""AVLTree: Self-balancing BST via height balance factor and rotations.

Run this file directly to execute the tests at the bottom.
"""
import random


class AVLTree:
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

    def _rotate_left(self, node):
        """_rotate_left"""
        raise NotImplementedError

    def _rotate_right(self, node):
        """_rotate_right"""
        raise NotImplementedError

    def _balance(self, node):
        """_balance"""
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


def test_avl_tree():

    t = AVLTree()
    for i in range(1, 1001):  # sorted input is the worst case for a plain BST
        t.insert(i)
    assert t.inorder() == list(range(1, 1001)) and len(t) == 1000
    assert t.height() <= 15, f"not balanced: height {t.height()}"
    for i in range(1, 1001, 2):
        assert t.delete(i)
    assert t.inorder() == list(range(2, 1001, 2)) and t.height() <= 15
    assert t.search(500) and not t.search(501)
    rng = random.Random(1)
    ref, t = set(), AVLTree()
    for _ in range(1000):
        x = rng.randint(0, 200)
        if rng.random() < 0.6:
            t.insert(x); ref.add(x)
        else:
            t.delete(x); ref.discard(x)
    assert t.inorder() == sorted(ref) and t.height() <= 2 * max(1, len(ref)).bit_length()


if __name__ == "__main__":
    test_avl_tree()
    print("AVLTree: all tests passed")
