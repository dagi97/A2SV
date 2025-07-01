# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class unionfind:
    def __init__(self,n):
        self.parent = {i:i for i in range(n)}
        self.rank = {i:0 for i in range(n)}

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            rankx, ranky = self.rank[rootx], self.rank[rooty]
            if rankx < ranky:
                self.parent[rootx] = rooty
            elif ranky < rankx:
                self.parent[rooty] = rootx
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
         
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dsu = unionfind(n)

        for u,v in edges:
            dsu.union(u,v)

        return  dsu.find(source) == dsu.find(destination)

        