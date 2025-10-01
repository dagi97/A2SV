# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        check = [1 ] * len(nums) 
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i + 1,  len(nums)):
                if nums[i] < nums[j]:
                    check[i] = max(check[i], check[j] + 1)
        return max(check)