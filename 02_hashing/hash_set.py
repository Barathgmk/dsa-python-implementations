"""HashSet: Set built on your HashMap.

Run this file directly to execute the tests at the bottom.
"""


class HashSet:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def add(self, x):
        """add"""
        raise NotImplementedError

    def remove(self, x):
        """remove"""
        raise NotImplementedError

    def contains(self, x):
        """contains"""
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


def test_hash_set():

    s = HashSet()
    assert len(s) == 0 and not s.contains(1)
    s.add(1); s.add(2); s.add(1)
    assert len(s) == 2 and s.contains(1) and s.contains(2)
    assert s.remove(1) and not s.remove(1)
    assert len(s) == 1 and not s.contains(1)
    for i in range(1000):
        s.add(i)
    assert len(s) == 1000 and all(s.contains(i) for i in range(1000))
    assert not s.contains(1000)


if __name__ == "__main__":
    test_hash_set()
    print("HashSet: all tests passed")
