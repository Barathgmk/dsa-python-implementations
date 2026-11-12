"""InvertedIndex: term -> postings list for document retrieval.

Conventions (the tests rely on these):
  Case-insensitive, whitespace tokenization. Searches return sorted doc ids.

Run this file directly to execute the tests at the bottom.
"""


class InvertedIndex:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def add_document(self, doc_id, text):
        """add_document"""
        raise NotImplementedError

    def search(self, term):
        """search"""
        raise NotImplementedError

    def search_and(self, terms):
        """search_and"""
        raise NotImplementedError

    def search_or(self, terms):
        """search_or"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_inverted_index():

    ix = InvertedIndex()
    ix.add_document(1, "the quick brown fox")
    ix.add_document(2, "The lazy brown dog")
    ix.add_document(3, "quick quick dog")
    assert ix.search("brown") == [1, 2]
    assert ix.search("QUICK") == [1, 3]
    assert ix.search("cat") == []
    assert ix.search_and(["quick", "dog"]) == [3]
    assert ix.search_and(["brown", "the"]) == [1, 2]
    assert ix.search_and(["quick", "cat"]) == []
    assert ix.search_or(["fox", "dog"]) == [1, 2, 3]
    assert ix.search_or(["cat"]) == []


if __name__ == "__main__":
    test_inverted_index()
    print("InvertedIndex: all tests passed")
