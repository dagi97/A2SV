# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def dp(i , j):
          
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[0][0]

            state = i,j

            if state not in memo:
                a = b = float('inf')
                if i + 1 < len(grid):
                    a = dp(i + 1, j) + grid[i + 1][j]
                if j + 1 < len(grid[0]):
                    b = dp(i, j + 1) + grid[i][j + 1]
                memo[state] = min(a, b)

            return memo[state]
        return dp(0, 0)  
            

        