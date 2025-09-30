# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def dp(i,sum_):
            if i == len(nums):
                return sum_== 0
            state = (i, sum_)
            if state not in memo:
                memo[state] = dp(i + 1, sum_- nums[i]) or dp(i + 1, sum_)
            return memo[state]

        target = sum(nums)//2
        
        return  sum(nums) % 2 == 0 and  dp(0, target)