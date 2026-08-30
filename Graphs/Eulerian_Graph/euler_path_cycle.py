"""
    https://www.geeksforgeeks.org/problems/euler-circuit-and-path/1

 1. Disconnected components can exist, but without edges
 2. EP will have exactly 2 vertices (start, end) with degree == 2
 3. EC is also an EP, but all degrees of all nodes are even numbered.
 4. If none of 1, 2 and 3 points are satisfied, then it is neither an EP, nor an EC.
"""
class Solution:
    def isEulerCircuit(self, V, adj):
    
        # Check whether all vertices having edges belong to one connected component.
        visited = set()
    
        def dfs(u):
            visited.add(u)
    
            for v in adj[u]:
                if v not in visited:
                    dfs(v)
    
        def is_connected():
            first_non_zero_degree_vertex = -1
    
            # Find any vertex that has at least one edge
            for u in range(V):
                if len(adj[u]) != 0:
                    first_non_zero_degree_vertex = u
                    break
    
            # No edges at all
            if first_non_zero_degree_vertex == -1:
                return True
    
            # DFS from that vertex
            dfs(first_non_zero_degree_vertex)
    
            # Every vertex with edges must be visited
            for u in range(V):
                if u not in visited and len(adj[u]) > 0:
                    return False
    
            return True
    
        # Count vertices having odd degree
        odd_degree_count = 0
    
        for u in range(V):
            if len(adj[u]) % 2 != 0:
                odd_degree_count += 1
    
        # Euler path/circuit requires all non-isolated vertices to be connected.
        if not is_connected():
            return 0

        # Neither EP nor EC
        if odd_degree_count > 2:
            return 0

        # Only EP
        if odd_degree_count == 2:
            return 1

        # odd_degree_count == 0 -> EC
        return 2