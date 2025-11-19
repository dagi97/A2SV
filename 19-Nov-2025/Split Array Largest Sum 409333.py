# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        low, high = max(nums), sum(nums)

        def isvalid(n):
            curr = 0
            c = 1
            for num in nums:
                if curr + num > n:
                    c += 1
                    curr = num
                    continue
                curr += num
            return c <= k


        while low <= high:
            mid = (low + high) // 2
            if isvalid(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
        