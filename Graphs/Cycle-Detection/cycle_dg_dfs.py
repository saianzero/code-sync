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


    def detect_cycle(self, adj, u, visited, in_recursion):

        visited.add(u)
        in_recursion.add(u)

        for v in adj[u]:

            if v in visited and v in in_recursion:
                return True
            
            if v not in visited:

                if self.detect_cycle(adj, v,  visited, in_recursion):
                    return True
        in_recursion.remove(u)
        return False
        

if __name__ == "__main__":
    V = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 1]]

    visited = set()
    in_recursion = set()

    new_graph = Graph(V, edges)
    adj = new_graph.build_adjacency_list()

    print(new_graph.detect_cycle(adj, 0, visited, in_recursion)) # parent of start vertex is assumed to be -1

