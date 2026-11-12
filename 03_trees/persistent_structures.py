"""PersistentList: Versioned immutable structure via path copying (e.g. persistent stack/BST).

Conventions (the tests rely on these):
  Immutable: every operation returns a new version and leaves old ones intact.

Run this file directly to execute the tests at the bottom.
"""


class PersistentList:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def push(self, x):
        """Return a NEW list with x on top; self is unchanged"""
        raise NotImplementedError

    def pop(self):
        """Return a NEW list without the top; IndexError if empty"""
        raise NotImplementedError

    def peek(self):
        """Top element; IndexError if empty"""
        raise NotImplementedError

    def to_list(self):
        """Elements bottom -> top"""
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


def test_persistent_structures():

    v0 = PersistentList()
    v1 = v0.push(1)
    v2 = v1.push(2)
    v3 = v2.pop()
    v4 = v2.push(99)  # branch off v2
    assert v0.to_list() == [] and len(v0) == 0
    assert v1.to_list() == [1]
    assert v2.to_list() == [1, 2] and v2.peek() == 2
    assert v3.to_list() == [1]
    assert v4.to_list() == [1, 2, 99]
    assert v2.to_list() == [1, 2]  # still unchanged
    _raises(IndexError, v0.pop)
    _raises(IndexError, v0.peek)


if __name__ == "__main__":
    test_persistent_structures()
    print("PersistentList: all tests passed")
