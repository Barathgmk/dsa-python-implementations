"""Stack: LIFO stack (backed by dynamic array or linked list).

Run this file directly to execute the tests at the bottom.
"""


class Stack:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def push(self, x):
        """push"""
        raise NotImplementedError

    def pop(self):
        """pop"""
        raise NotImplementedError

    def peek(self):
        """peek"""
        raise NotImplementedError

    def is_empty(self):
        """is_empty"""
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


def test_stack():

    s = Stack()
    assert s.is_empty() and len(s) == 0
    for i in (1, 2, 3):
        s.push(i)
    assert s.peek() == 3 and len(s) == 3 and not s.is_empty()
    assert s.pop() == 3 and s.pop() == 2 and s.pop() == 1
    assert s.is_empty()
    _raises(IndexError, s.pop)
    _raises(IndexError, s.peek)


if __name__ == "__main__":
    test_stack()
    print("Stack: all tests passed")
