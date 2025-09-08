# Problem: Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        freq = {}
        left = 0
        distinct_count = 0
        ans = 0
        n = len(nums)

        for right in range(n):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            if freq[nums[right]] == 1:
                distinct_count += 1
            while distinct_count == k:
                ans += n - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct_count -= 1
                left += 1
        return ans
