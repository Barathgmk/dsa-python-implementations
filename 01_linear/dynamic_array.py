"""DynamicArray: Resizable array (amortized O(1) append). Use a fixed-size backing list; double capacity when full.

Run this file directly to execute the tests at the bottom.
"""


class DynamicArray:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def append(self, x):
        """Add to end"""
        raise NotImplementedError

    def insert(self, i, x):
        """Insert at index, shift right"""
        raise NotImplementedError

    def pop(self, i=-1):
        """Remove and return"""
        raise NotImplementedError

    def get(self, i):
        """get"""
        raise NotImplementedError

    def set(self, i, x):
        """set"""
        raise NotImplementedError

    def __len__(self):
        """__len__"""
        raise NotImplementedError

    def _resize(self, cap):
        """Copy into new backing store"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_dynamic_array():

    a = DynamicArray()
    for i in range(100):
        a.append(i)
    assert len(a) == 100 and a.get(0) == 0 and a.get(99) == 99
    a.insert(0, -1)
    assert a.get(0) == -1 and a.get(1) == 0 and len(a) == 101
    a.insert(len(a), 500)
    assert a.get(len(a) - 1) == 500
    assert a.pop() == 500
    assert a.pop(0) == -1 and a.get(0) == 0
    a.set(5, "x")
    assert a.get(5) == "x"
    _raises(IndexError, a.get, len(a))
    _raises(IndexError, a.get, -1)
    _raises(IndexError, DynamicArray().pop)


if __name__ == "__main__":
    test_dynamic_array()
    print("DynamicArray: all tests passed")
