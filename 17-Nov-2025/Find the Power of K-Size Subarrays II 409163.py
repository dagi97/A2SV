# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums

        c = 0
        ans = []

        for i in range(1, k):
            if nums[i] != nums[i-1] + 1:
                c += 1

        ans.append(nums[k-1] if c == 0 else -1)

        for r in range(k, n):
            if nums[r-k+1] != nums[r-k] + 1:
                c -= 1
            if nums[r] != nums[r-1] + 1:
                c += 1
            ans.append(nums[r] if c == 0 else -1)

        return ans
