# Problem: Array With Elements Not Equal to Average of Neighbors - https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        l, r = 0, len(nums) - 1 
        while l < r:
            ans.append(nums[l])
            ans.append(nums[r])
            l += 1
            r -= 1
        if l == r:
            ans.append(nums[r])
        return ans
        