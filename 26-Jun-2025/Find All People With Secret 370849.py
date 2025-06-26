# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dsu = UnionFind(n)
        dsu.union(0, firstPerson)
        meetings = sorted(meetings, key= lambda x:x[2])
        time = 0
        ans = {0, firstPerson}

        for u, v, t in meetings:
            if t != time:
                for i in ans:
                    if dsu.find(i) != dsu.find(0):
                        dsu.parent[i] = i
                ans = set()
                time = t
        
            dsu.union(u, v)
            ans.update({u,v})
        
        return [i for i in range(n) if dsu.find(i) == dsu.find(0)]