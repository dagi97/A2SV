# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        def isValid(mid):
            count = 0
            check = 0 
            
            for r in range(len(weights)):
                check += weights[r]
                if check > mid:
                    check = weights[r]
                    count += 1
                 
            return count 
           
        while low <= high:
            mid = (low+ high) // 2
            if isValid(mid) < days:
                high = mid - 1
            else:
                low = mid + 1
        return low
        