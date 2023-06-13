import networkx as nx
import random
from exponencial import can_be_made_bipartite
from fpt1 import bipartization
from aprox_sol import grasp_bipartization
from colorama import Fore

def generate_test_cases(n, k_min, k_max):
    
    for _ in range(n):
        # Generate random graph 
        G = nx.erdos_renyi_graph(random.randint(10, 20), 0.5)
        
        # Generate random solution size
        k = random.randint(k_min, k_max)  
        
        # Find optimal solution
        fpt = bipartization(G, k)
 
        exp = grasp_bipartization(G, k, 10)

        print(Fore.WHITE, f"Test case:{k=}")
        if fpt == exp:
            print(Fore.GREEN, exp ,"==" , fpt )
        else:
            print(Fore.RED, fpt,"==", exp)

def specific_cases():

    # Grafo completo con n nodos
    n = 10
    G = nx.complete_graph(n)
    k = n**2//4
    iterations = 10

    fpt = bipartization(G, k)
 
    exp = grasp_bipartization(G, k, 30)

    if fpt == exp:
        print(Fore.GREEN, exp ,"==" , fpt )
    else:
        print(Fore.RED, fpt,"==", exp)

    # Grafo bipartito con n nodos, m aristas y probabilidad p
    n = 10
    m = 20
    p = 0.5
    graph = nx.bipartite.random_graph(n, m, p)
    k = m
    iterations = 10
    
    fpt = bipartization(G, k)
 
    exp = grasp_bipartization(G, k, 30)

    if fpt == exp:
        print(Fore.GREEN, exp ,"==" , fpt )
    else:
        print(Fore.RED, fpt,"==", exp)

    # Grafo en forma de estrella con n nodos
    n = 10
    graph = nx.star_graph(n-1)
    k = n-1

    fpt = bipartization(G, k)
    exp = grasp_bipartization(G, k, 30)

    if fpt == exp:
        print(Fore.GREEN, exp ,"==" , fpt )
    else:
        print(Fore.RED, fpt,"==", exp)

    # Grafo en forma de ciclo con n nodos
    n = 10
    graph = nx.cycle_graph(n)
    k = n//2

    fpt = bipartization(G, k)
    exp = grasp_bipartization(G, k, 30)

    if fpt == exp:
        print(Fore.GREEN, exp ,"==" , fpt )
    else:
        print(Fore.RED, fpt,"==", exp)

# Genera c casos con k entre km y ka
C = 3
km = 0
ka = 10

generate_test_cases(C, km, ka)
specific_cases()
