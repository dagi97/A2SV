# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        check = ((n*(n+1))//2)
        s = 0
        for i in nums:
            s += i
        return check - s

        
        