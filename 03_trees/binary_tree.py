"""BinaryTree: Binary tree node + traversals.

Conventions (the tests rely on these):
  height counts nodes on the longest root-leaf path; diameter counts edges. Traversals return lists.

Run this file directly to execute the tests at the bottom.
"""


class BinaryTree:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def inorder(self):
        """inorder"""
        raise NotImplementedError

    def preorder(self):
        """preorder"""
        raise NotImplementedError

    def postorder(self):
        """postorder"""
        raise NotImplementedError

    def level_order(self):
        """BFS"""
        raise NotImplementedError

    def height(self):
        """height"""
        raise NotImplementedError

    def diameter(self):
        """diameter"""
        raise NotImplementedError

    @staticmethod
    def from_list(values):
        """Static: build from level-order list, None = missing (like LeetCode)"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_binary_tree():

    t = BinaryTree.from_list([1, 2, 3, 4, 5])
    assert t.inorder() == [4, 2, 5, 1, 3]
    assert t.preorder() == [1, 2, 4, 5, 3]
    assert t.postorder() == [4, 5, 2, 3, 1]
    assert t.level_order() == [1, 2, 3, 4, 5]
    assert t.height() == 3 and t.diameter() == 3
    sparse = BinaryTree.from_list([1, None, 2, None, 3])
    assert sparse.inorder() == [1, 2, 3] and sparse.height() == 3 and sparse.diameter() == 2
    empty = BinaryTree.from_list([])
    assert empty.inorder() == [] and empty.height() == 0 and empty.level_order() == []


if __name__ == "__main__":
    test_binary_tree()
    print("BinaryTree: all tests passed")
