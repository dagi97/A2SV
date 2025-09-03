# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

class unionfind:
    def __init__(self, n):
        self.parent = {i:i for i in range (1, n + 1)}
        self.rank = {i:0 for i in range(1, n + 1)}
        self.pt = {i:0 for i in range(1, n + 1)}
   
    def find(self, x):
        
        if self.parent[x] != x:
            x = self.find(self.parent[x])
        return x

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)

        if rootx != rooty:
            rankx, ranky = self.rank[rootx], self.rank[rooty]

          
            if ranky > rankx:
                self.parent[rootx] = rooty
                self.pt[rootx] -= self.pt[rooty]
            elif rankx > ranky:
                self.parent[rooty] = rootx
                self.pt[rooty] -= self.pt[rootx]
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
                self.pt[rooty] -= self.pt[rootx]
    def add (self, x , val):
        root = dsu.find(x)
        self.pt[root] += val
    def get (self,x, ans):
        while self.parent[x] != x:
            ans += self.pt[x]
            x = self.parent[x]
        ans += self.pt[x]

        return ans
        
    



n, k = map(int, input().split())
dsu = unionfind(n)
for _ in range(k):
    arr = list(map(str, input().split()))
    if arr[0] == 'join':
        dsu.union(int(arr[1]), int(arr[2]))
    elif arr[0] == 'add':
        dsu.add(int(arr[1]), int(arr[2]))
    else:
        print(dsu.get(int(arr[1]), 0))
