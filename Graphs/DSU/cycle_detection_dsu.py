class Solution:
    def detectCycle(self, V, adj):
        rank = [0] * V
        parent = list(range(V))

        def isCycle(V):
            for u in range(V):
                for v in adj[u]:
                    if u < v:
                        u_root = find(u, parent)
                        v_root = find(v, parent)

                        if u_root == v_root:
                            return True

                        union(u, v, parent)

            return False

        
        def find(x, parent):
            if x == parent[x]:
                return x

            parent[x] = find(parent[x], parent)
            return parent[x]

        def union(x, y, parent):
            x_root = find(x, parent)
            y_root = find(y, parent)

            if x_root == y_root:
                return False

            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root

            elif rank[x_root] < rank[y_root]:
                parent[x_root] = y_root

            else:
                parent[x_root] = y_root
                rank[y_root] += 1

            return

        return isCycle(V)