# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        c = 0 
        a, b, d = -1, -1, -1

        for i in range(len(nums)):
            if nums[i] == minK:
                a = i
            if nums[i] == maxK:
                b = i
            elif nums[i] < minK or nums[i] > maxK:
                d = i
            c += max(0, min(a,b) - d )
        return c

        