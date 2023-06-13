from itertools import product
import networkx as nx

def can_be_made_bipartite(G, k):
    # Enumerar todas las biparticiones posibles
    V = set(G.nodes())
    bipartitions = [(set(a), V-set(a)) for a in product(V, repeat=len(V))]

    # Verificar cuántas aristas deben eliminarse para cada bipartición
    candidates = []
    for A, B in bipartitions:
        count = 0
        for u in A:
            for v in G[u]:
                if v in A:
                    count += 1
        for u in B:
            for v in G[u]:
                if v in B:
                    count += 1
        count //= 2  # eliminar aristas duplicadas
        if count <= k:
            candidates.append((A, B))

    # Verificar si hay candidatos posibles
    if candidates:
        return True
    else:
        return False