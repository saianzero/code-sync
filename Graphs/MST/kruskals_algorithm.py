"""
Kruskal's Algorithm

1. Sort the edges by weight in ascending order
2. Start processing from the smallest weight.
3. For the corresponding u,v - if parents are diff -> disconnected, so we connect u,v
4. Each time we connect, update the res with the weight. 
5. res is the sum of weights of the MST

"""

class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        # code here
        parent = list(range(V))
        rank = [0]*V
        
        edges = sorted(edges, key = lambda x: x[2])
        
        def find(x):
            
            if x == parent[x]:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
            
        def union(x,y):
            
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return
            
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
                
            else:
                 parent[root_x] = root_y
                 rank[root_y] += 1
                
        res = 0    
        for u, v, w in edges:
            pu = find(u)
            pv = find(v)
            
            if pu != pv:
                union(u,v)
                res+=w
        
        return res