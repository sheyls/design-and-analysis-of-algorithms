import networkx as nx

def create_graph():
    n, m = map(int, input().split()) 
    graph = nx.DiGraph()
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.add_edge(u, v, weight=w, inv=False)
        graph.add_edge(v, u, weight=w, inv=True)
    return graph

# Encontramos el camino de costo mínimo entre dos nodos

def min_cost_path(graph, source, target): 
    path = nx.dijkstra_path(graph, source, target, weight='weight')
    cost = nx.dijkstra_path_length(graph, source, target, weight='weight')
    print(path)
    print(cost)
    return path, cost

def inv_edges(graph: nx.DiGraph, path):
    inverted_edges = []
    cost = 0
    for i in range(len(path)-1):
        edge = graph.get_edge_data(path[i], path[i+1])
        if edge['inv']:
            inverted_edges.append((path[i], path[i+1]))
            cost = max(cost, edge["weight"])
    
    return inverted_edges, cost

def all_to_all():

g = create_graph()
p, cost = min_cost_path(g,1,2)
i, i_cost = inv_edges(g, p)