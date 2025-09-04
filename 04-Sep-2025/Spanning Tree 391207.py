# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

class unionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(1, n + 1)}
        self.rank = {i:0 for i in range(1,n + 1)}
        

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)

        if rootx != rooty:
            rankx, ranky = self.rank[rootx], self.rank[rooty]

            if ranky > rankx:
                self.parent[rootx] = rooty
               
            elif rankx > ranky:
                self.parent[rooty] = rootx
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            return True
        return False
n, m = map(int, input().split())
graph = []
dsu = unionFind(n)

for _ in range (m):
    b, e, w =  map(int, input().split())
    graph.append([w,b,e])

graph.sort()
c = 0
e = 0

for w, u , v in graph:
    if  dsu.union(u, v):
        c += w
        e += 1
        if e == n-1 :
            break
print(c)

