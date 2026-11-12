"""SuffixTree: Suffix tree (Ukkonen, or naive first).

Run this file directly to execute the tests at the bottom.
"""
import random


class SuffixTree:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def build(self, s):
        """build"""
        raise NotImplementedError

    def contains(self, pattern):
        """contains"""
        raise NotImplementedError

    def count(self, pattern):
        """count"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_suffix_tree():

    st = SuffixTree()
    st.build("banana")
    assert st.contains("nan") and st.contains("banana") and st.contains("a")
    assert not st.contains("nab") and not st.contains("xyz")
    assert st.count("a") == 3 and st.count("ana") == 2 and st.count("na") == 2
    assert st.count("banana") == 1 and st.count("xyz") == 0
    rng = random.Random(9)
    s = "".join(rng.choice("ab") for _ in range(100))
    st = SuffixTree(); st.build(s)
    for pat in ("a", "ab", "ba", "aab", "abab", "bbbb"):
        assert st.count(pat) == sum(s.startswith(pat, i) for i in range(len(s)))


if __name__ == "__main__":
    test_suffix_tree()
    print("SuffixTree: all tests passed")
