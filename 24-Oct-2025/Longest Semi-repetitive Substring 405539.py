# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
        c  = 0
        ans = 0
        n = len(s)
        l, r = 0, 1 
        if n == 1:
            return 1

        while  r < n:
            if s[r-1] == s[r]:
                c += 1
            while c > 1:
                if s[l] == s[l + 1]:
                    c -= 1
                l += 1
            ans = max(ans, r-l + 1)
            r += 1


         
        return ans

        