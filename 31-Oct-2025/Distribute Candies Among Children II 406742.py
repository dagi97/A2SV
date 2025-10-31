# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(limit, n) + 1):
            start = max(n - limit - i, 0 )
            end = min(n - i, limit)
            res += max(end - start  + 1, 0)
        return res
         
        

        