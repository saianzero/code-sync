from collections import defaultdict, deque

class Graph:

    def __init__(self, V, edges):
        self.V = V
        self.edges = edges

    def build_adjacency_list(self):
        adj = defaultdict(list)

        for u,v in self.edges:
            adj[u].append(v)
            # adj[v].append(u) #uncomment for undirected graph

        return adj


    def bfs(self, adj, u, visited):
        q = deque()
        q.append(u)
        visited.add(u)

        while q:
            u =  q.popleft()
            res.append(u)
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v) 
    


        
if __name__ == "__main__":
    V = 4
    edges = [[1, 0], [2, 0], [2, 1], [3, 1]]

    # optimize this later
    res = [] 
    visited = set()

    new_graph = Graph(V, edges)
    adj = new_graph.build_adjacency_list()

    new_graph.bfs(adj, 2, visited)

    print(res)

