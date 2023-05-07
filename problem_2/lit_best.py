import networkx as nx
import networkx as nx
import numpy as np
from utils import create_graph, invert_edges
import numpy as np
from utils import create_graph, is_capital


def add_edges_lt_c(graph: nx.DiGraph, c: int):
    graph = graph.copy()
    for u, v, w in graph.edges.data("weight"):
        if w <= c:
            graph.add_edge(v, u, weight=w)
    return graph


def try_max_inv_cost(graph: nx.DiGraph, c: int):
    graph = add_edges_lt_c(graph, c)
    min_cost, cap = np.inf, -1
    for n in graph.nodes:
        cost = is_capital(graph, n)
        if cost != -1 and cost + c < min_cost:
            cap = n
            min_cost = cost + c
    return min_cost, cap


def solution(graph: nx.DiGraph):
    possible_c = sorted(list(set([edge[-1] for edge in graph.edges.data("weight")])))
    min_cost, capital = np.inf, -1
    for c in possible_c:
        cost, cap = try_max_inv_cost(graph, c)
        print(cost, cap)
        if cap == -1:
            continue
        if cost < min_cost:
            min_cost, capital = cost, cap
    return min_cost, capital


n, m = 4, 4
weights = [(2, 1, 3), (3, 2, 50), (2, 4, 2), (4, 3, 1)]
g = create_graph(n, m, weights)
print(solution(g))
