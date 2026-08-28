# https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

"""
    Bellman ford algo is a follow up to Dijkstra.
    
    Dikstra can work with both Directed as well as Undirected graphs, 
    but Bellman Ford only with DIRECTED.
    Dijkstra CANNOT work with negative weights/edges.
    Dijkstra CANNOT detect a negative cycle.

    Given a DIRECTED weighted (negative weights allowed) graph, relax 'V' total vertices'V-1' number of times 
    to get the shortest path from the given source. Further relaxations would not change the result;
    But if it does- you have detected a negative cycle.

"""

class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        # Q asked us to use 10**8 explicitly, else float("inf").
        res = [int(1e8)]*V
        res[src] = 0

        # Relax V-1 times
        for i in range(V-1):
            for u, v, w in edges:
                # if you cannot reach u itself, no point in trying to reach v via u.
                if res[u] != int(1e8) and res[u]+w < res[v]:
                    res[v] = res[u]+w

        # Relax one more time - Vth time to detect cycle.
        for u, v, w in edges:
             if res[u] != int(1e8) and res[u]+w < res[v]:
                 return [-1]
        
        return res