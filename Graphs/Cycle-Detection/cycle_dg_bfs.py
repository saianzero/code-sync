from collections import defaultdict, deque

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

    def build_indegree_list(self, indegree):

        for _,v in self.edges:
            indegree[v]+=1

        return indegree


    def detect_cycle(self, adj, indegree, count = 0):

        q =  deque()

        for u in range(self.V):
            if indegree[u] == 0:
                q.append(u)
                count+=1

        while q:

            u = q.popleft()

            for v in adj[u]:
                indegree[v]-=1
                if indegree[v] == 0:
                    q.append(v)
                    count+=1

        if count == self.V:
            return False
        else: 
            return True

if __name__ == "__main__":
    V = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 1]]

    indegree = [0]*V    
    new_graph = Graph(V, edges)
    adj = new_graph.build_adjacency_list()
    indegree = new_graph.build_indegree_list(indegree)
    print(new_graph.detect_cycle(adj, indegree, 0))

