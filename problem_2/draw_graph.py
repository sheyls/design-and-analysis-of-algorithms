import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo vacío
G = nx.DiGraph()

# Agregar los nodos existentes
G.add_nodes_from([1, 2, 3])

# Agregar el nodo duplicado
G.add_node(1, pos=(0,1))

# Agregar las aristas existentes
G.add_edges_from([(1,2), (2,3)])

# Agregar la nueva arista desde el nodo 3 al nodo duplicado 1
G.add_edge(3, 1, pos=(0,0))

# Definir la posición de cada nodo en el dibujo del grafo
pos = {1: (0,1), 2: (1,0), 3: (2,1)}

# Definir el color de cada arista
edge_color = ['blue', 'blue', 'red']

# Dibujar el grafo
nx.draw(G, pos, with_labels=True, edge_color=edge_color, arrowsize=20)

# Mostrar el dibujo del grafo
plt.show()
