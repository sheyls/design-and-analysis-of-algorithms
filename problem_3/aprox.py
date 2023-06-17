import random
import networkx as nx

def random_bipartization(graph, k, iterations=30):
    """
    Elimina k aristas aleatorias del grafo y verifica si el grafo resultante es bipartito.
    Si es así, devuelve el subgrafo bipartito resultante. Si no, se repite el proceso.
    """
    for _ in range(iterations):
        edges = random.sample(graph.edges(), k=k)
        temp_graph = graph.copy()
        temp_graph.remove_edges_from(edges)
        if nx.is_bipartite(temp_graph):
            return True
    return False
    
