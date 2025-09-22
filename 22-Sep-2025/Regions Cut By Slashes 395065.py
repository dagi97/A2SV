# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = n * 3
        expanded = [[0] * size for _ in range(size)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    expanded[i*3][j*3+2] = 1
                    expanded[i*3+1][j*3+1] = 1
                    expanded[i*3+2][j*3] = 1
                elif grid[i][j] == '\\':
                    expanded[i*3][j*3] = 1
                    expanded[i*3+1][j*3+1] = 1
                    expanded[i*3+2][j*3+2] = 1

        def dfs(x, y):
            if x < 0 or y < 0 or x >= size or y >= size or expanded[x][y] != 0:
                return
            expanded[x][y] = 1
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        regions = 0
        for i in range(size):
            for j in range(size):
                if expanded[i][j] == 0:
                    regions += 1
                    dfs(i, j)
        return regions
