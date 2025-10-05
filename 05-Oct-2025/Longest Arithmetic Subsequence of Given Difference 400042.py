# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = {}
        ans = 0

        for i in arr:
            dp[i] = dp.get(i- difference, 0) + 1
            ans = max(ans, dp[i])
        return ans

        