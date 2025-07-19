# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class unionFind:
    def __init__(self):
        self.parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
    def find(self, x):
        if self.parent[x] != x:
          self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return 
        
        if ord(rootx) < ord(rooty):
            self.parent[rooty] = rootx
        else:
            self.parent[rootx] = rooty
    
    
      



class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = unionFind()
        for i in range(len(s1)):
            dsu.union(s1[i],s2[i])
        
        ans = ''
        for i in baseStr:
            a = dsu.find(i)
            ans += a
        return ans
    
        