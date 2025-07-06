# Problem: Minimize Maximum of Array - https://leetcode.com/problems/minimize-maximum-of-array/

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        a = 0
        c = 0
        for i, v in enumerate(nums):
            c += v
            a = max(a, ceil(c/( i + 1) ))
             
        return a


        
        