# DAG ONLY

from collections import defaultdict

class Graph:

    def __init__(self, V, edges):
        self.V = V
        self.edges = edges

    def build_adjacency_list(self):
        adj = defaultdict(list)

        for u,v in self.edges:
            adj[u].append(v)
            # adj[v].append(u) # for undirected graph

        return adj


    def topological_sort(self, adj, u, visited, stack):

        visited.add(u)

        for v in adj[u]:
            if v not in visited:
                self.topological_sort(adj,v, visited, stack)

        stack.append(u)
    

        

if __name__ == "__main__":
    V = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

    visited = set()
    stack = []

    new_graph = Graph(V, edges)
    adj = new_graph.build_adjacency_list()

    for i in range(V):
        if i not in visited:
            new_graph.topological_sort(adj, i, visited, stack)
    print(stack[::-1])

