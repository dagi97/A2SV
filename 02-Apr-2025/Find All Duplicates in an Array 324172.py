# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            n = abs(num)
            if nums[n-1] < 0:
                res.append(n)
            nums[n-1] = -nums[n-1]
        return res

        