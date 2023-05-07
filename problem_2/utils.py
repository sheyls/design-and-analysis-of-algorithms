from typing import Iterable, List, Tuple
import networkx as nx


def graph_from_input():
    n, m = map(int, input().split())
    weights = []
    for _ in range(m):
        weights.append(tuple(map(int, input().split())))
    return create_graph(n, m, weights)


def create_graph(n: int, m: int, weights: List[Tuple[int, int, int]]):
    graph = nx.DiGraph()
    for u, v, w in weights:
        graph.add_edge(u, v, weight=w)
    return graph


def invert_edges(graph: nx.DiGraph, edges: List[Tuple[int, int, int]]) -> nx.DiGraph:
    graph = graph.copy()
    max_weight = 0
    for u, v, w in edges:
        max_weight = max(max_weight, w)
        graph.remove_edge(u, v)
        graph.add_edge(v, u, weight=w)
    return graph, max_weight


def is_capital(graph: nx.DiGraph, node: int) -> int:
    edges_used = {}
    for n, paths in dict(nx.all_pairs_dijkstra_path(graph)).items():
        # print(n, paths)
        if node not in paths:
            return -1
        for i in range(len(paths[node]) - 1):
            u, v = paths[node][i], paths[node][i + 1]
            edges_used[(u, v)] = graph.edges[u, v]["weight"]
    return sum(edges_used.values())
