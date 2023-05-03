from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if visited[v] == False and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

    def find_min_cost_path(self):
        # Find the maximum flow from the source to the sink
        max_flow = self.ford_fulkerson(0, self.V - 1)

        # Invert all edges with positive flow to find the minimum cost path
        for u in range(self.V):
            for v in self.graph[u]:
                if self.graph[u][v] == 0:
                    self.graph[u][v] = float("Inf")
                elif self.graph[u][v] > 0:
                    self.graph[u][v] = -self.graph[u][v]

        # Find the shortest path from any node to any other node using Dijkstra's algorithm
        dist = [float("Inf")] * self.V
        dist[0] = 0
        visited = [False] * self.V

        for i in range(self.V):
            u = None
            for j in range(self.V):
                if not visited[j] and (u is None or dist[j] < dist[u]):
                    u = j
            visited[u] = True

            for v in self.graph[u]:
                if dist[u] != float("Inf") and dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]

        # Return the negative of the shortest path distance from