import networkx as nx
from itertools import combinations


def bipartization(G, k):
    if nx.is_bipartite(G):
        return True
    
    cuts = find_cuts(G, k)  
    
    for cut in cuts: 
        # Eliminar corte del grafo
        H = G.copy()
        H.remove_edges_from(cut)  
                
        # Chequear si sigue siendo bipartito
        if nx.is_bipartite(H):  
            print(cut)
            return True
        
    return False

def find_cuts(G, k):
    # Generar todos los subconjuntos de tamaño k
    cuts = []
    edges = list(G.edges()) 
    for i in range(1, k+1):
        for subset in combinations(edges, i):
            cuts.append(subset) 
   # print(cuts)
    return cuts
