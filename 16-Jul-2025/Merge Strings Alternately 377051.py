# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        a, b = len(word1), len(word2)
        l, r =  0, 0

        while l < a and r<b:
            ans += word1[l]
            ans += word2[r]
            l += 1
            r += 1
        ans += word1[l:]
        ans += word2[r:]
        return ans
      
        