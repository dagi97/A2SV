# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        c = 0

        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr = gcd(curr, nums[j])

                if curr == k:
                    c += 1
                elif curr < k:
                    break
        return c
        