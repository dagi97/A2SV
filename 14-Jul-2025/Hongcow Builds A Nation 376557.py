# Problem: Hongcow Builds A Nation - https://codeforces.com/contest/744/problem/A

from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(1,n+1)}
        self.size = {i:1 for i in range(1,n+1)}
    def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)

        if xr == yr:
            return 
        if xr in l or yr in l:
            if xr in l:
                self.parent[yr] = xr
                self.size[xr] += self.size[yr]
                
            elif yr in l:
                self.parent[xr] = yr
                self.size[yr] += self.size[xr]
        else:


            if self.size[xr] < self.size[yr]:
                self.parent[xr] = yr
                self.size[yr] += self.size[xr]
            else:
                self.parent[yr] = xr
                self.size[xr] += self.size[yr]
        
n,v,k = map(int, input().split())
l = set(map(int, input().split())) 
dsu = UnionFind(n)
for _ in range(v):
    x,y = map(int, input().split())
    dsu.union(x,y)
p = -1
c = float("-inf")
for i in l:
   check =  dsu.find(i)
   if dsu.size[check] > c:
       c = dsu.size[check]
       p = check
 

ans = 0
lst = defaultdict(set)
 
for j in range(1, n+ 1):
    lst[dsu.find(j)].add(j)
naughtyset = set()
for i in lst:
    if i in l:
        for j in lst[i]:
            naughtyset.add(j)
 

for j in range(1,n+1):
    if dsu.find(j) != dsu.find(p) and j not in l and j not in naughtyset:
        ans += 1
        dsu.union(j,dsu.find(p))
exisitingedges = ans + v
totaledge = 0
zaz = set()

for j in range(1, n+ 1):
    parent = dsu.find(j)
 
    if parent not in zaz:
        zaz.add(dsu.find(j))
        o = dsu.size[parent]
        totaledge +=int((o * (o-1))/2)
        
 
print(totaledge- exisitingedges + ans)


 





