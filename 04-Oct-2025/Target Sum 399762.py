# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def dp(i, total):

            if i == len(nums):
                return 1 if target == total else 0
            
            state = i, total

            if state not in memo:
                memo[state] = dp(i + 1, total + nums[i] ) +  dp(i + 1, total - nums[i])
            return memo[state]
        return dp(0, 0)

            
        