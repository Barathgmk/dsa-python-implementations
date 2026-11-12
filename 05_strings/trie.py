"""Trie: Prefix tree.

Run this file directly to execute the tests at the bottom.
"""


class Trie:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def insert(self, word):
        """insert"""
        raise NotImplementedError

    def search(self, word):
        """search"""
        raise NotImplementedError

    def starts_with(self, prefix):
        """starts_with"""
        raise NotImplementedError

    def delete(self, word):
        """delete"""
        raise NotImplementedError

    def autocomplete(self, prefix):
        """autocomplete"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_trie():

    t = Trie()
    for w in ("apple", "app", "application", "apt", "bat"):
        t.insert(w)
    assert t.search("app") and t.search("apple") and not t.search("appl") and not t.search("ap")
    assert t.starts_with("appl") and t.starts_with("b") and not t.starts_with("c")
    assert t.autocomplete("app") == ["app", "apple", "application"]
    assert t.autocomplete("z") == []
    assert t.autocomplete("") == ["app", "apple", "application", "apt", "bat"]
    assert t.delete("app")
    assert not t.search("app") and t.search("apple") and t.starts_with("app")
    assert not t.delete("app") and not t.delete("nope")
    assert t.delete("bat") and not t.starts_with("b")


if __name__ == "__main__":
    test_trie()
    print("Trie: all tests passed")
