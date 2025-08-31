# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

class Solution:
    def friendRequests(self, n, restrictions, requests):
        dsu = DSU(n)
        result = []
        
        for u, v in requests:
            ru, rv = dsu.find(u), dsu.find(v)
            if ru == rv:
                result.append(True)
                continue
            
            # check restrictions
            can_merge = True
            for x, y in restrictions:
                rx, ry = dsu.find(x), dsu.find(y)
                if (rx == ru and ry == rv) or (rx == rv and ry == ru):
                    can_merge = False
                    break
            
            if can_merge:
                dsu.union(ru, rv)
                result.append(True)
            else:
                result.append(False)
        
        return result
