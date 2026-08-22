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
            # adj(v).append(u) # for undirected

        return adj

    # works for both directed and undirected
    def build_adjacency_list_from_matrix(matrix):
        adj = defaultdict(list)

        for u in range(len(matrix)):
            for v in range(len(matrix[u])):
                if matrix[u][v] == 1:
                    adj[u].append(v)

        return adj

if __name__ == "__main__":
    V = 4 # No. of vertices (V)
    edges = [[1, 0], [2, 0], [2,1], [3,1]]

    new_graph = Graph(V, edges)
    print(new_graph.build_adjacency_list())