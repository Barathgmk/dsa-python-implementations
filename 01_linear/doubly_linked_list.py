"""DoublyLinkedList: Doubly linked list with sentinel head/tail. Basis for LRU, deque, browser history.

Conventions (the tests rely on these):
  push_front/push_back return the new node; nodes expose `.val`; pops return values; empty pop -> IndexError.

Run this file directly to execute the tests at the bottom.
"""


class DoublyLinkedList:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def push_front(self, x):
        """push_front"""
        raise NotImplementedError

    def push_back(self, x):
        """push_back"""
        raise NotImplementedError

    def pop_front(self):
        """pop_front"""
        raise NotImplementedError

    def pop_back(self):
        """pop_back"""
        raise NotImplementedError

    def remove_node(self, node):
        """O(1) unlink given node"""
        raise NotImplementedError

    def move_to_front(self, node):
        """move_to_front"""
        raise NotImplementedError

    def __len__(self):
        """__len__"""
        raise NotImplementedError

    def __iter__(self):
        """__iter__"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_doubly_linked_list():

    d = DoublyLinkedList()
    n2 = d.push_back(2); n1 = d.push_front(1); n3 = d.push_back(3)
    assert list(d) == [1, 2, 3] and len(d) == 3
    assert n2.val == 2
    d.remove_node(n2)
    assert list(d) == [1, 3] and len(d) == 2
    d.move_to_front(n3)
    assert list(d) == [3, 1]
    assert d.pop_back() == 1 and d.pop_front() == 3 and len(d) == 0
    _raises(IndexError, d.pop_front)
    _raises(IndexError, d.pop_back)
    d.push_back(5)
    assert list(d) == [5]


if __name__ == "__main__":
    test_doubly_linked_list()
    print("DoublyLinkedList: all tests passed")
