# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            nums[abs(i)-1] = -1 * abs(nums[abs(i)-1])
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res


        
        