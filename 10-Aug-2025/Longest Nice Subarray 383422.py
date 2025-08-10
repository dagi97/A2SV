# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        mask = 0  
        max_len = 0
        
        for right, num in enumerate(nums):
            
            while mask & num:
                mask ^= nums[left]  
                left += 1
            
            
            mask |= num
            
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
