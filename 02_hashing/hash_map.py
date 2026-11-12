"""HashMap: Hash table with chaining (then try open addressing). Implement resizing on load factor.

Conventions (the tests rely on these):
  get returns None if missing; remove returns True/False.

Run this file directly to execute the tests at the bottom.
"""


class HashMap:
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

    def contains(self, k):
        """contains"""
        raise NotImplementedError

    def _hash(self, k):
        """_hash"""
        raise NotImplementedError

    def _resize(self):
        """Rehash into larger table"""
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


def test_hash_map():

    m = HashMap()
    assert len(m) == 0 and m.get("a") is None
    m.put("a", 1); m.put("b", 2)
    assert m.get("a") == 1 and len(m) == 2
    m.put("a", 10)
    assert m.get("a") == 10 and len(m) == 2
    assert m.contains("b") and not m.contains("z")
    assert m.remove("b") and not m.remove("b") and len(m) == 1
    for i in range(2000):
        m.put(i, i * i)
    assert len(m) == 2001 and all(m.get(i) == i * i for i in range(2000))
    for i in range(0, 2000, 2):
        m.remove(i)
    assert len(m) == 1001 and m.get(2) is None and m.get(3) == 9
    m.put((1, 2), "t")
    assert m.get((1, 2)) == "t"


if __name__ == "__main__":
    test_hash_map()
    print("HashMap: all tests passed")
