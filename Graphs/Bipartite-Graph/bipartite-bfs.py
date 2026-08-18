from collections import defaultdict, deque
class Solution:
    def isBipartite(self, V, edges):
        color = [-1]*V

        def check_bipartite_BFS(adj, V, color):

            q = deque()
            for u in range(V):
                if color[u] == -1:
                    q.append(u)
                    color[u] = 0
                # check for each connected component (a disconnected graph also bipartite)
                # A graph is bipartite if every connected component is bipartite.
                    while q:
                        u = q.popleft()
                        curr_color = color[u]

                        for v in adj[u]:
                            if color[v] == curr_color:
                                return False

                            if color[v] == -1:
                                color[v] = 1 - curr_color
                                q.append(v)

            return True

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return check_bipartite_BFS(adj, V, color)

