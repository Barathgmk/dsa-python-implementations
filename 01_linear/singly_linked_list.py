"""SinglyLinkedList: Singly linked list with head pointer (add tail for O(1) append).

Run this file directly to execute the tests at the bottom.
"""


class SinglyLinkedList:
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

    def remove(self, x):
        """Delete first occurrence"""
        raise NotImplementedError

    def find(self, x):
        """find"""
        raise NotImplementedError

    def reverse(self):
        """In-place reversal"""
        raise NotImplementedError

    def has_cycle(self):
        """Floyd fast/slow"""
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


def test_singly_linked_list():

    l = SinglyLinkedList()
    assert len(l) == 0 and list(l) == []
    l.push_back(2); l.push_back(3); l.push_front(1)
    assert list(l) == [1, 2, 3] and len(l) == 3
    assert l.find(2) and not l.find(9)
    assert l.remove(2) and not l.remove(2)
    assert list(l) == [1, 3]
    l.push_back(4); l.reverse()
    assert list(l) == [4, 3, 1]
    assert l.pop_front() == 4 and list(l) == [3, 1]
    assert not l.has_cycle()
    m = SinglyLinkedList()
    m.push_back(1); m.push_back(2); m.remove(2); m.push_back(3)  # tail pointer must be updated
    assert list(m) == [1, 3]
    m.remove(1); m.remove(3)
    assert len(m) == 0
    _raises(IndexError, m.pop_front)


if __name__ == "__main__":
    test_singly_linked_list()
    print("SinglyLinkedList: all tests passed")
