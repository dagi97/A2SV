# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mydict = defaultdict(int)
        check = set()
        if not trust and n== 1:
            return 1
        for a,b in trust:
            check.add(a)
            mydict[b] += 1
        for k,v in mydict.items():
            if v == n-1 and k not in check:
                return k
        return -1
            
      
        