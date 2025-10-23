# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

class unionfind:
    def __init__(self, n):
        self.parent = {i:i for i in range (1, n + 1)}
        self.size = {i:1 for i in range(1, n + 1)}
        self.min_ = {i:i for i in range(1, n + 1)}
        self.max_ = {i:i for i in range(1, n + 1)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union (self, x, y):
        rootx, rooty = self.find(x), self.find(y)

        if rootx == rooty:
            return
        if self.size[rootx] > self.size[rooty]:
            self.size[rootx] += self.size[rooty]
            self.parent[rooty] = self.parent[rootx]
            self.min_[rootx] = min(self.min_[rootx], self.min_[rooty] )
            self.max_[rootx] = max(self.max_[rooty], self.max_[rootx])

        else:
            self.size[rooty] += self.size[rootx]
            self.parent[rootx] = self.parent[rooty]
            self.min_[rooty] = min(self.min_[rootx], self.min_[rooty] )
            self.max_[rooty] = max(self.max_[rooty], self.max_[rootx])

    def get(self, x):
        root = self.find(x)
        return self.min_[root], self.max_[root], self.size[root]







n, k = map(int, input().split())
dsu = unionfind(n)
for _ in range(k):
    arr = list(map(str, input().split()))
    if arr[0] == 'union':
        dsu.union(int(arr[1]), int(arr[2]))
    else:
        a, b, c = dsu.get(int(arr[1]))
        print(a, b, c)