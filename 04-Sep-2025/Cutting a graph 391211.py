# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D


class unionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(1, n+ 1)}
        self.rank = {i:0 for i in range(1, n + 1)}

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
    

     
n,m,k = map(int, input().split())
dsu = unionFind(n)
check = []
for _ in range(m):
    u, v = map(int, input().split())
for _ in range(k):
    op, u, v = map(str, input().split())
    u = int(u)
    v = int(v)
    check.append((op,u,v))
check.reverse()
ans = []
for op, u, v in check:
    if op == 'ask':
        if dsu.find(u) == dsu.find(v):
            ans.append('YES')
             
        else:
            ans.append('NO')
    else:
        dsu.union(u,v)
 
while ans:
    print(ans.pop())
