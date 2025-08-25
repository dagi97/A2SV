# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, o, c):
            if len(curr) == 2 * n:
                ans.append(curr)
                return 
            if o < n:
                backtrack(curr + '(', o + 1, c)
            if c < o:
                backtrack(curr + ')' , o, c + 1)
        ans = []
        backtrack("",0,0)
        return ans
