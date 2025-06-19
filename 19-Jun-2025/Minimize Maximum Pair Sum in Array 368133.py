# Problem: Minimize Maximum Pair Sum in Array - https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0, len(nums) - 1
        c = 0
        while l < r:
            check = nums[l] + nums[r]
            l += 1
            r -= 1
            c = max( c, check)
        return c