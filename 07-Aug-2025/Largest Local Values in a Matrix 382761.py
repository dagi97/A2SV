# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

 

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = []

        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                max_val = max(
                    grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
                )
                row.append(max_val)
            result.append(row)
        
        return result
