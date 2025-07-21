# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        check = set()
        c = 0
        l = 0
        for i in s:
            if i in check:
                c += 1
                check.clear()
                
            check.add(i)
           
        return c + 1

      
      