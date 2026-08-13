from collections import defaultdict, deque

class Graph:

    def __init__(self, V, edges):
        self.V = V
        self.edges = edges

    def build_adjacency_list(self):
        adj = defaultdict(list)

        for u,v in self.edges:
            adj[u].append(v)
            adj[v].append(u) # for undirected graph

        return adj


    def detect_cycle(self, adj, u, visited, parent):

        q = deque()
        q.append((u, parent))
        visited.add(u)

        while q:
            u, parent = q.popleft()
            for v in adj[u]:
                if v == parent:
                    continue
                if v in visited:
                    return True
                visited.add(v)
                q.append((v,u))
                         
        return False

        

if __name__ == "__main__":
    V = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 1]]

    visited = set()

    new_graph = Graph(V, edges)
    adj = new_graph.build_adjacency_list()

    print(new_graph.detect_cycle(adj, 0, visited, -1)) # parent of start vertex is assumed to be -1

