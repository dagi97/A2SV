# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo = {}

        def dp(i, j):

            state = (i, j)

            if i == len(triangle) - 1:
                return triangle[i][j]

            if state not in memo:
                memo[state] = min(dp(i + 1 , j  + 1), dp(i + 1, j) )+ triangle[i][j]

            return memo[state]
        return dp(0, 0)

 
        