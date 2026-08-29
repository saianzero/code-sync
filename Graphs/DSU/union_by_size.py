class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) # [0,1,2,3,4,...,n-1]
        self.size = [1]*n

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

        # Path compression
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x] 

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        # union by size
        if self.size[x_root] > self.size[y_root]:
            self.parent[y_root] = x_root
            self.size[x_root]+=self.size[y_root]

        elif self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root]+=self.size[x_root]

        else:
            self.parent[x_root] = y_root
            self.size[y_root]+=self.size[x_root]
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