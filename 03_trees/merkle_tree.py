"""MerkleTree: Hash tree for data integrity; supports proofs.

Conventions (the tests rely on these):
  Leaves are strings. verify(root, leaf, proof) is static; proof format is yours.

Run this file directly to execute the tests at the bottom.
"""


class MerkleTree:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def build(self, leaves):
        """build"""
        raise NotImplementedError

    def root(self):
        """root"""
        raise NotImplementedError

    def proof(self, i):
        """Sibling hashes path"""
        raise NotImplementedError

    @staticmethod
    def verify(root, leaf, proof):
        """Static"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_merkle_tree():

    leaves = ["a", "b", "c", "d", "e"]  # odd count on purpose
    m = MerkleTree(); m.build(leaves)
    m2 = MerkleTree(); m2.build(leaves)
    assert m.root() == m2.root()
    m3 = MerkleTree(); m3.build(["a", "b", "c", "d", "X"])
    assert m3.root() != m.root()
    for i, leaf in enumerate(leaves):
        assert MerkleTree.verify(m.root(), leaf, m.proof(i))
    assert not MerkleTree.verify(m.root(), "tampered", m.proof(0))
    assert not MerkleTree.verify(m3.root(), "a", m.proof(0))
    one = MerkleTree(); one.build(["only"])
    assert MerkleTree.verify(one.root(), "only", one.proof(0))


if __name__ == "__main__":
    test_merkle_tree()
    print("MerkleTree: all tests passed")
