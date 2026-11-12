"""GraphList: Graph via adjacency list (directed/undirected, weighted).

Conventions (the tests rely on these):
  neighbors returns [(v, w)] in insertion order. bfs/dfs return visit order (neighbors in insertion order, recursive-DFS order). dijkstra returns {vertex: dist}.

Run this file directly to execute the tests at the bottom.
"""


class GraphList:
    def __init__(self, directed=False):
        # TODO: set up internal state
        raise NotImplementedError

    def add_edge(self, u, v, w=1):
        """add_edge"""
        raise NotImplementedError

    def neighbors(self, u):
        """neighbors"""
        raise NotImplementedError

    def bfs(self, s):
        """bfs"""
        raise NotImplementedError

    def dfs(self, s):
        """dfs"""
        raise NotImplementedError

    def connected_components(self):
        """connected_components"""
        raise NotImplementedError

    def dijkstra(self, s):
        """dijkstra"""
        raise NotImplementedError

    def add_vertex(self, u):
        """Add isolated vertex"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_graph_adjacency_list():

    g = GraphList()
    for u, v in [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]:
        g.add_edge(u, v)
    assert g.neighbors(0) == [(1, 1), (2, 1)]
    assert [v for v, _ in g.neighbors(3)] == [1, 2, 4]
    assert g.bfs(0) == [0, 1, 2, 3, 4]
    assert g.dfs(0) == [0, 1, 3, 2, 4]
    d = GraphList(directed=True)
    d.add_edge(0, 1); d.add_edge(1, 2)
    assert d.neighbors(1) == [(2, 1)] and d.neighbors(2) == []
    assert d.bfs(2) == [2]
    c = GraphList()
    for u, v in [(0, 1), (1, 2), (3, 4)]:
        c.add_edge(u, v)
    c.add_vertex(5)
    assert sorted(sorted(comp) for comp in c.connected_components()) == [[0, 1, 2], [3, 4], [5]]
    w = GraphList()
    for u, v, wt in [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]:
        w.add_edge(u, v, wt)
    w.add_edge(8, 9, 1)
    dist = w.dijkstra(0)
    assert dist[0] == 0 and dist[2] == 1 and dist[1] == 3 and dist[3] == 4
    assert dist.get(8, float("inf")) == float("inf")


if __name__ == "__main__":
    test_graph_adjacency_list()
    print("GraphList: all tests passed")
