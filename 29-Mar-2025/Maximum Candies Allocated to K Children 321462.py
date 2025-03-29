# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
    
        def isValid(candy):
            count = 0
            for i in candies:
                    count += i // candy
            return count >= k

        low = 1
        high = max(candies)

        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                low = mid + 1
            else:
                high = mid - 1
       
        return high
        