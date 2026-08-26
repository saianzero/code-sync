from collections import defaultdict
import heapq
class Solution:
    def shortestPath(self, V, edges, src, dest):
        
        res = [float("inf")]*(V+1)
        res[src] = 0
        parent = list(range(V+1))

        min_heap = [[0,src]]

        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])

        while min_heap:

            d,u = heapq.heappop(min_heap)

            if d > res[u]:
                continue

            for v,w in adj[u]:
                if d+w < res[v]:
                    res[v] = d+w
                    parent[v] = u
                    heapq.heappush(min_heap, [res[v],v])

        if res[dest] == float("inf"):
            return [-1]

        node = dest
        path = []
        while parent[node] != node:
            path.append(node)
            node = parent[node]

        path.append(src)
        return path[::-1]

        """_summary_
        Return the shortest path, (if multiple paths exist for same shortest path- return any one)
        """