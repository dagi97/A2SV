# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []

        def backtrack(curr):
            if len(curr) == n:
                result.append(curr)
                return 
            if not curr or curr[-1] == "1":
                backtrack(curr + '0')
                backtrack(curr + '1')
            else:
                backtrack(curr + '1')
        backtrack('')
        return result
        