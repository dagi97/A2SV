# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        dsu = UnionFind(n)
        
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                d = []
                for l in range(len(strs[0])):
                    if strs[i][l] != strs[j][l]:
                        d.append(l)
                if len(d) == 2 and strs[i][d[0]] == strs[j][d[1]] and strs[i][d[1]] == strs[j][d[0]]:
                    dsu.union(i, j)
                elif len(d) == 0:
                    dsu.union(i, j)
        
        for i in range(n):
            dsu.find(i)

        

        return len(set(dsu.parent))


        
        