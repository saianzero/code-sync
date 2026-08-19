from collections import defaultdict


class Graph:
    def __init__(self, V, edges):
        self.V = V
        self.edges = edges

    def build_adjacency_list(self):
        adj = defaultdict(list)
        # adj["u"] returns [], .append(v)
        
        for u, v in self.edges:
            # u ---edge---> v
            adj[u].append(v)

        return adj

if __name__ == "__main__":
    V = 4 # No. of vertices (V)
    edges = [[1, 0], [2, 0], [2,1], [3,1]]

    new_graph = Graph(V, edges)
    print(new_graph.build_adjacency_list())