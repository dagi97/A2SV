# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        check = Counter(s)
        c = 0
        if len(set(s)) == 1:
            return len(s)
        for k, v in check.items():


                c += v // 2
        c *= 2
        if c < len(s):
            return c + 1
        return c 
