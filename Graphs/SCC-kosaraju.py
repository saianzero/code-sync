"""
https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1

Count of Strongly Connected Components - Kosaraju's Agorithm

1. Topological sort -> stack maintains the order (reverse the stack)
2. Reverse the edge directions of the entire directed graph
3. Perform DFS on every non-visited vertex and count+=1 for each dfs
"""

from collections import defaultdict
class Solution:

    def kosaraju(self, V, edges):
        stack = []
        adj = defaultdict(list)
        visited= set()
        
        
        for u,v in edges:
            adj[u].append(v)
        
        def topo_sort(adj, u, visited, stack):
            visited.add(u)
            
            for v in adj[u]:
                if v not in visited:
                    topo_sort(adj, v, visited, stack)
            
            stack.append(u)
            
        
        def dfs(adj, u, visited):
            visited.add(u)
            
            for v in adj[u]:
                if v not in visited:
                    dfs(adj,v,visited)
            
        
        
        #Step 1
        for u in range(V):
            if u not in visited:
                topo_sort(adj, u, visited, stack)
        
        
        # step 2
        rev_adj = defaultdict(list)
        for u,v in edges:
            rev_adj[v].append(u)
            
        stack = stack[::-1]
        
        res = 0
        visited = set()
        for u in stack:
            if u not in visited:
                dfs(rev_adj, u, visited)
                res+=1
        return res
        
        
        
        
        
        
        
        
            
                    