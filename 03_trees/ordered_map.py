"""OrderedMap: Sorted key-value map on top of a balanced BST.

Conventions (the tests rely on these):
  get/floor/ceiling return None when nothing matches; range returns sorted keys in [lo, hi].

Run this file directly to execute the tests at the bottom.
"""


class OrderedMap:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def put(self, k, v):
        """put"""
        raise NotImplementedError

    def get(self, k):
        """get"""
        raise NotImplementedError

    def remove(self, k):
        """remove"""
        raise NotImplementedError

    def floor(self, k):
        """Largest key <= k"""
        raise NotImplementedError

    def ceiling(self, k):
        """Smallest key >= k"""
        raise NotImplementedError

    def range(self, lo, hi):
        """Keys in [lo, hi]"""
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


def test_ordered_map():

    m = OrderedMap()
    for k in (5, 1, 9, 3, 7):
        m.put(k, str(k))
    assert len(m) == 5 and m.get(3) == "3" and m.get(4) is None
    assert m.floor(6) == 5 and m.floor(5) == 5 and m.floor(0) is None
    assert m.ceiling(6) == 7 and m.ceiling(9) == 9 and m.ceiling(10) is None
    assert m.range(3, 7) == [3, 5, 7] and m.range(10, 20) == [] and m.range(0, 100) == [1, 3, 5, 7, 9]
    m.put(5, "five")
    assert m.get(5) == "five" and len(m) == 5
    assert m.remove(5) and not m.remove(5)
    assert m.floor(6) == 3 and m.ceiling(4) == 7 and len(m) == 4


if __name__ == "__main__":
    test_ordered_map()
    print("OrderedMap: all tests passed")
