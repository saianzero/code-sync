from collections import defaultdict
import heapq

class Solution:
    def dijkstra(self, V: int, edges: list[list[int]], src: int) -> list[int]:

        res = [float("inf")]*V
        res[src] = 0
        
        min_heap = [[0, src]]

        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        while min_heap:
            
            d,u = heapq.heappop(min_heap)
            
            # (Optimization) skip stale heap entries
            # d: src -> u distance, res[u] : min distance from src to u, so far
            if d > res[u]:
                continue
            
            for v, w in adj[u]:
                # d+w: src -(d)-> u -(w)-> v
                if d+w < res[v]:
                    res[v] = d+w
                    heapq.heappush(min_heap, (res[v],v))
                
        return res
        
        """
        Min distance bw nodes in Undirected Weighted Graph
        Summary:
        1. Initialize res with inf values
        2. Initialize min_heap with [0, source], i.e. source to source is 0 weight
        3. adj list for u,v,w
        4. regular BFS code, while min_heap (here min_heap is the priority queue):
            4.1 pop the min from queue (min_heap pop will return min), store d, u
            4.2 check for each neighbours of u
            4.3 if total dist < res[neighbour] - 
                update new minimum distance and push to min_heap
        5.return res
        
        Note: Ordered set doesn't exist in Python

        TC- approx. O(V.logV)

        """