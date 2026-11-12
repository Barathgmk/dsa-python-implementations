"""DAG: Directed acyclic graph with cycle detection and topological sort.

Conventions (the tests rely on these):
  topological_sort raises ValueError if there is a cycle.

Run this file directly to execute the tests at the bottom.
"""


class DAG:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def add_edge(self, u, v):
        """add_edge"""
        raise NotImplementedError

    def has_cycle(self):
        """has_cycle"""
        raise NotImplementedError

    def topological_sort(self):
        """Kahn and DFS versions"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_dag():

    g = DAG()
    for u, v in [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]:
        g.add_edge(u, v)
    assert not g.has_cycle()
    order = g.topological_sort()
    assert sorted(order) == [0, 1, 2, 3, 4, 5]
    pos = {v: i for i, v in enumerate(order)}
    for u, v in [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]:
        assert pos[u] < pos[v]
    g.add_edge(1, 5)  # 5 -> 2 -> 3 -> 1 -> 5
    assert g.has_cycle()
    _raises(ValueError, g.topological_sort)


if __name__ == "__main__":
    test_dag()
    print("DAG: all tests passed")
