# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys
import threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
class unionfind:
    def __init__(self,n):
        self.parent = {i:i for i in range(1,n + 1)}
        self.rank = {i:0 for i in range(1, n + 1)}
       
         
    def find(self, x):
        if x == -1 :
            return -1    
        if self.parent[x] != x :
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        
        rankx = self.rank[rootx]
        ranky = self.rank[rooty]

        if rankx > ranky:
            self.parent[rooty] = rootx
           
        elif ranky > rankx:
            self.parent[rootx] = rooty
             
        else:
            self.parent[rootx] = rooty
            self.rank[rooty] += 1
    def go(self, x):
        if x != n:
            self.parent[x] = self.find(x+1)
        else:
            self.parent[x] = -1
           

n, m = map(int, input().split())
dsu = unionfind(n)
for i in range(m):
    op, val =  map(str, input().split())
    val = int(val)
   
   
    if op == '?':
        print(dsu.find(val))
        
    else:
        dsu.go(val)
 

