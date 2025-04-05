# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        ind = 0
        ans = 0
        for i in range(row):
            count = 0
            for j in range(col):
                if mat[i][j]== 1:
                    count += 1
            if count > ans:
                ans = count
                ind = i
        return (ind,ans)
            

        