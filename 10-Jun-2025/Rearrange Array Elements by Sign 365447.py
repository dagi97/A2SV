# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        l, r = 0, 1
        for num in nums:
            if num > 0:
                result[l] = num
                l += 2
            else:
                result[r] = num
                r += 2
        return result