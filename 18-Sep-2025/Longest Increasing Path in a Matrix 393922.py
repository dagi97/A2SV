# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r , c = len(matrix) , len(matrix[0])
        arr = [[0]* c for i in range(r)]
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(x, y):
            return 0 <= x < r and 0 <= y < c  

        def dfs(r, c):
            ans = 1
            if arr[r][c]:
                return arr[r][c]

            for dx , dy in dir:
                nr, nc = r + dx ,c + dy
                if inbound(nr, nc) and matrix[nr][nc] > matrix[r][c]:
                    ans = max(ans, 1 + dfs(nr, nc))
            arr[r][c] = ans
            return ans
        
        res =  0
        for i in range(r):
            for j in range(c):
                    res = max(res, dfs(i,j))
        return res




        