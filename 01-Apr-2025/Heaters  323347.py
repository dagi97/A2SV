# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def isValid(rad):
            l, r = 0, 0 
            while l < len(houses) and r < len(heaters) :
                if abs(houses[l] - heaters[r]) <= rad:
                    l += 1
                else:
                    r += 1
            return l == len(houses) 

        low = 0
        high = max(houses[-1],heaters[-1])
        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low 
