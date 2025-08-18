# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = set(), set()
        ro,co = len(matrix), len(matrix[0])
        for i in range(ro):
            for j in range(co):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)

        for i in range(ro):
            for j in range(co):
                if i in r or j in c:
                    matrix[i][j] = 0
        