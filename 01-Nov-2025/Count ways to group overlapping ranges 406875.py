# Problem: Count ways to group overlapping ranges - https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:

        ranges.sort()
        c = 0
        check = -1
         
        
        for i in range(len(ranges)):
            s, e = ranges[i]
            if s > check:
                c += 1
                check = e
            else:
                check = max(check , e)
            
            
        
                
         
        
        return  pow(2, c, 10**9 + 7)
        



        



        