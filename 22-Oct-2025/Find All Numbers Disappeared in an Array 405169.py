# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            ind = nums[i] - 1
            if nums[i] != nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
            else:
                i += 1

     
        out = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                out.append(i + 1)
        
        return out