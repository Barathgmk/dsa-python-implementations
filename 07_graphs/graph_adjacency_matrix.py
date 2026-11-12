"""GraphMatrix: Graph via adjacency matrix (dense graphs).

Conventions (the tests rely on these):
  neighbors returns ascending vertex ids; floyd_warshall returns a matrix using float('inf') for no path.

Run this file directly to execute the tests at the bottom.
"""


class GraphMatrix:
    def __init__(self, n, directed=False):
        # TODO: set up internal state
        raise NotImplementedError

    def add_edge(self, u, v, w=1):
        """add_edge"""
        raise NotImplementedError

    def has_edge(self, u, v):
        """has_edge"""
        raise NotImplementedError

    def neighbors(self, u):
        """neighbors"""
        raise NotImplementedError

    def floyd_warshall(self):
        """floyd_warshall"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_graph_adjacency_matrix():

    g = GraphMatrix(4)
    g.add_edge(0, 1); g.add_edge(1, 2)
    assert g.has_edge(0, 1) and g.has_edge(1, 0) and not g.has_edge(0, 2)
    assert g.neighbors(1) == [0, 2] and g.neighbors(3) == []
    d = GraphMatrix(4, directed=True)
    d.add_edge(0, 1, 3); d.add_edge(1, 2, 2); d.add_edge(0, 2, 10); d.add_edge(2, 3, 1)
    assert d.has_edge(0, 1) and not d.has_edge(1, 0)
    dist = d.floyd_warshall()
    inf = float("inf")
    assert dist[0][2] == 5 and dist[0][3] == 6 and dist[1][3] == 3
    assert dist[3][0] == inf and dist[2][1] == inf
    assert all(dist[i][i] == 0 for i in range(4))


if __name__ == "__main__":
    test_graph_adjacency_matrix()
    print("GraphMatrix: all tests passed")
