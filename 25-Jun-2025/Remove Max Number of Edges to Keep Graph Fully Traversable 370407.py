# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        self.count -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsu_a = UnionFind(n)
        dsu_b = UnionFind(n)
        c = 0
        for t, u, v in edges:
            if t == 3:
                b = dsu_b.union(u,v)
                a = dsu_a.union(u,v)
                if not a and not b:
                    c += 1
        for t,u, v in edges:
            if t == 1:
                a = dsu_a.union(u,v)
                if not a:
                    c += 1
        for t, u, v in edges:
            if t == 2:
                b = dsu_b.union(u,v)
                if not b:
                    c += 1
        if dsu_a.count>1  or dsu_b.count >  1:
            return -1
        return c
