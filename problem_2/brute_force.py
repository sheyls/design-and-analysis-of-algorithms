from math import e
import networkx as nx
from typing import Iterable, List, Tuple
from itertools import chain, combinations
import numpy as np
from utils import create_graph, invert_edges


def powerset(iterable: Iterable) -> List[Tuple]:
    s = list(iterable)
    res = []
    for i in range(len(s) + 1):
        res += combinations(s, i)
    return res


def solution(graph: nx.DiGraph):
    min_cost = np.inf
    capital = -1
    for edges in powerset(graph.edges.data("weight", default=100)):
        # print(edges)
        g, inv_cost = invert_edges(graph, edges)
        # print(inv_cost)
        for n in graph.nodes:
            # print(f'Trying capital: {n}')
            capital_cost = is_capital(g, n)

            # if capital_cost != -1:
            # print(f"Final cost {capital_cost + inv_cost}")
            if capital_cost != -1 and capital_cost + inv_cost < min_cost:
                capital = n
                min_cost = capital_cost + inv_cost
    return min_cost, capital


n, m = 4, 4
weights = [(2, 1, 3), (3, 2, 50), (2, 4, 2), (4, 3, 1)]
g = create_graph(n, m, weights)
print(solution(g))
