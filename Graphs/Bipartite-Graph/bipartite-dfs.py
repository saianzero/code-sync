from collections import defaultdict

class Solution:
    def isBipartite(self, V, edges):

        def check_bipartite_DFS(adj, u, color, currColor):
            color[u] = currColor

            for v in adj[u]:
                if color[v] == currColor:
                    return False
                if color[v] == -1:
                    color[v] == 1 - currColor

                if not check_bipartite_DFS(adj, v, color, color[v]):
                    return False
            return True

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        color = [-1]*V

        # color1 = 1
        # color0 = 0

        for i in range(V):
            if color[i] == -1: # unvisited
                # say we start with color1
                if not check_bipartite_DFS(adj, i, color, 1): 
                    return False

        return True