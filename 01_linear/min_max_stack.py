"""MinStack: Stack with O(1) get_min (and variant get_max).

Conventions (the tests rely on these):
  Empty pop/top -> IndexError.

Run this file directly to execute the tests at the bottom.
"""


class MinStack:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def push(self, x):
        """push"""
        raise NotImplementedError

    def pop(self):
        """pop"""
        raise NotImplementedError

    def top(self):
        """top"""
        raise NotImplementedError

    def get_min(self):
        """get_min"""
        raise NotImplementedError

    def get_max(self):
        """get_max"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_min_max_stack():

    s = MinStack()
    for x in (3, 1, 2):
        s.push(x)
    assert s.top() == 2 and s.get_min() == 1 and s.get_max() == 3
    assert s.pop() == 2 and s.get_min() == 1
    assert s.pop() == 1 and s.get_min() == 3 and s.get_max() == 3
    s.push(3)
    s.push(0)
    assert s.get_min() == 0
    s.pop()
    assert s.get_min() == 3
    s.pop(); s.pop()
    _raises(IndexError, s.pop)
    _raises(IndexError, s.top)


if __name__ == "__main__":
    test_min_max_stack()
    print("MinStack: all tests passed")
