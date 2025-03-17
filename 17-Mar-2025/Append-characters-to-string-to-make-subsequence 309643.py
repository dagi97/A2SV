# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l, r = 0, 0
        count = len(t)
        while r < len(s) and l < len(t):
            if s[r] == t[l]:
                count -= 1
                r += 1
                l += 1
            else:
                r += 1
            
        return count
            

