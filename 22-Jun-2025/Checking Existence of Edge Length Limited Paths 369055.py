# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            self.parent[self.find(x)] = self.find(y)

        def connected(self, x, y):
            return self.find(x) == self.find(y)

class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        edgeList.sort(key=lambda x: x[2]) 
        queries = sorted([(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)], key=lambda x: x[2])

        dsu = UnionFind(n)
        res = [False] * len(queries)
        i = 0 

        for p, q, limit, idx in queries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                dsu.union(edgeList[i][0], edgeList[i][1])
                i += 1
            res[idx] = dsu.connected(p, q)

        return res

        