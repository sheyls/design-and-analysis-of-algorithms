import random
from networkx.algorithms import bipartite
import networkx as nx

def grasp_bipartization(graph, k, iterations):
    
    if graph.number_of_edges() == 0 or nx.is_bipartite(graph):
        return True
    
    for i in range(iterations):
        # Generar solución inicial aleatoria
        solution = []
        for edge in graph.edges():
            if random.random() < 0.5:
                solution.append(edge)
                
        # Seleccionar aleatoriamente k aristas y eliminarlas del grafo original
        if len(solution) > k:
            subgraph_edges = random.sample(solution, k)
        else:
            subgraph_edges = solution
            
        subgraph = nx.Graph()
        subgraph.add_edges_from(subgraph_edges)

        if subgraph.number_of_edges() == 0:
            return len(solution) <= k
    
        
        # Mejorar la solución utilizando búsqueda local
        improved_subgraph = local_search(subgraph)

        
        # Aplicar un algoritmo de búsqueda de subgrafos bipartitos para encontrar un subgrafo bipartito
        # dentro del subgrafo actual
        if nx.is_bipartite(improved_subgraph) and nx.is_connected(improved_subgraph):
            X, Y = bipartite.sets(improved_subgraph)
            if len(X) > len(Y):
                X, Y = Y, X
            edges_to_remove = []
            for edge in improved_subgraph.edges():
                if edge[0] in Y and edge[1] in X:
                    edges_to_remove.append(edge)
            improved_subgraph.remove_edges_from(edges_to_remove)
            
        # Actualizar la mejor solución encontrada
        deleted_edges = len(solution) - len(improved_subgraph.edges())
        return deleted_edges <= k

            
    #eturn best_solution, min_deleted_edges

def local_search(subgraph, iter):
   
    for _ in range(iter):
        # Buscar un par de nodos que no estén conectados y que si se conectaran generarían un subgrafo bipartito
        try:
            X, Y = bipartite.sets(subgraph)
        except:
            return subgraph
            
        if len(X) > len(Y):
            X, Y = Y, X
        for u in X:
            for v in Y:
                if not subgraph.has_edge(u, v):
                    neighbors_u = set(subgraph.neighbors(u))
                    neighbors_v = set(subgraph.neighbors(v))
                    common_neighbors = neighbors_u.intersection(neighbors_v)
                    if common_neighbors.issubset(X.union(Y)):
                        # Conectar los nodos u y v para obtener un subgrafo bipartito
                        subgraph.add_edge(u, v)
                        # Eliminar todas las aristas entre nodos de X o de Y para mantener la bipartición
                        for x in X:
                            for y in Y:
                                if subgraph.has_edge(x, y):
                                    subgraph.remove_edge(x, y)
                        for y in Y:
                            for z in Y:
                                if subgraph.has_edge(y, z):
                                    subgraph.remove_edge(y, z)
                        return subgraph
        else:
            # Si no se encontró un par de nodos que mejorara la solución, terminar la búsqueda local
            return subgraph
