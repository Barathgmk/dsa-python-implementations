"""RadixTree: Compressed trie (Patricia): edges hold strings.

Run this file directly to execute the tests at the bottom.
"""


class RadixTree:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def insert(self, key):
        """insert"""
        raise NotImplementedError

    def search(self, key):
        """search"""
        raise NotImplementedError

    def starts_with(self, prefix):
        """starts_with"""
        raise NotImplementedError

    def delete(self, key):
        """delete"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_radix_tree():

    r = RadixTree()
    words = ["romane", "romanus", "romulus", "rubens", "ruber", "rubicon", "rubicundus"]
    for w in words:
        r.insert(w)
    assert all(r.search(w) for w in words)
    assert not r.search("rom") and not r.search("rubic") and not r.search("")
    assert r.starts_with("rom") and r.starts_with("roman") and r.starts_with("rub")
    assert not r.starts_with("romani") and not r.starts_with("x")
    r.insert("rube")
    assert r.search("rube") and r.search("ruber") and r.search("rubens")
    assert r.delete("romane")
    assert not r.search("romane") and r.search("romanus") and r.starts_with("roman")
    assert not r.delete("romane")


if __name__ == "__main__":
    test_radix_tree()
    print("RadixTree: all tests passed")
