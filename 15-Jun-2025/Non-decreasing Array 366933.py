# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        l, r = 0, 1
        check = deepcopy(nums)
        while r < len(nums):

            if nums[l] > nums[r]:
                nums[l] = nums[r]
                check[r] = check[l]
                break
            l += 1
            r += 1
        return nums == sorted (nums) or check == sorted (check)