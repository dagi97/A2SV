# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)  
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for w in wordDict:
                a = i + len(w)
                if  a <= n and s[i : a] == w:
                    dp[i] = dp[a]
                if dp[i]:
                    break
       
        return dp[0]

        

        
        