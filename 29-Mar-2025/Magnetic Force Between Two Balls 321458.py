# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        def isValid(force):
            p.sort()
            curr = p[0]
            c = 0
            for i in range(1,len(p)):
                if p[i] - curr >= force:
                    c += 1
                    curr = p[i]
             
            return c + 1 >= m




        low = 1
        high = max(p) - min(p)
        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
      