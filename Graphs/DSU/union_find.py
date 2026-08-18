class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) # [0,1,2,3,4,...,n-1]

        # Each node starts as the root of its own separate set: 
        # 0 → 0
        # 1 → 1
        # 2 → 2
        # 3 → 3
        # 4 → 4

    def find(self, x):
        # Find the root
        if x == self.parent[x]:
            return x

        # return self.find(self.parent[x]) # unoptimized

        # Path compression
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x] 

    def union(self, x, y):
        # Find roots
        x_root = self.find(x)
        y_root = self.find(y)

        # Already in the same set
        if x_root == y_root:
            return False

        # Join the two sets
        self.parent[x_root] = y_root
        return True


# Example
uf = UnionFind(5)

uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

print(uf.find(0))  # 2
print(uf.find(2))  # 2
print(uf.find(3))  # 4
print(uf.find(4))  # 4

print(uf.find(0) == uf.find(2))  # True
print(uf.find(0) == uf.find(3))  # False