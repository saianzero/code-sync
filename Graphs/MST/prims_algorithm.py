"""
https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

Given a weighted, undirected, and connected graph with V vertices and a 2D array edges[][], where each element edges[i] = [u, v, w] represents an edge between vertices u and v with weight w, 

return the 
        sum of the weights of all edges 
                        in the graph's Minimum Spanning Tree (MST).
"""

import heapq
from collections import defaultdict

class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:

        res = 0 # min edge weight sum
        visited = set()
        
        min_heap = [[0,0]]  # w, node; we need the min "w" hence min_heap
        
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
            
        while min_heap: # TC - O(E)
            w,u = heapq.heappop(min_heap) # TC- O(log(E))
            
            if u in visited:
                continue
            visited.add(u)
            
            res+=w # update the min edge weight sum with the min weight "W" for the node "u"
            
            for v,w in adj[u]:
                if v not in visited:
                    heapq.heappush(min_heap, [w,v]) # TC- O(log(E))
                    
        
        return res

    # Total TC - O(E.log(E)), E - no. of Edges