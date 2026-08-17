# Kahn's Ago: Topological sort using BFS
# Only works for Directed ACYCLIC Graph (detect cycles)

from collections import deque, defaultdict

class Graph:
    def __init__(self, V, edges):
        self.V = V
        self.edges = edges

    def build_adj_list(self, edges):
        adj =  defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
        return adj
    

    def build_indegree_list(self, edges, indegree):
            for u,v in edges:
                indegree[v]+=1
            return indegree


    def bfs(self, V, adj, indegree, res):

        q = deque()

        for u in range(V):
            if indegree[u] == 0:
                q.append(u)


        while q:
            u = q.popleft()
            res.append(u)

            for v in adj[u]:
                indegree[v]-=1

                if indegree[v] == 0:
                    q.append(v)
        return res

if __name__ == "__main__":
    V = 6

    edges = [[0,3], [0,2], [1,4], [2,1], [2,3], [3,1], [5,1], [5,4]]

    indegree = [0]*V

    res = []

    new_graph = Graph(V, edges)

    adj = new_graph.build_adj_list(edges)

    indegree = new_graph.build_indegree_list(edges, indegree)









                





