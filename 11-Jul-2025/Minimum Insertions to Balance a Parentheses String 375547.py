# Problem: Minimum Insertions to Balance a Parentheses String - https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        c = 0
        j  = 0 
        while j < len(s):
            i = s[j]
            if i == '(':
                stack.append(i)
                j += 1
            else:
                if j + 1 < len(s) and s[j+1] == ')':
                    if stack:
                        stack.pop()
                    else:
                        c += 1
                    j += 2
                else:
                    if not stack:
                        c += 2
                    else:
                        c += 1
                        stack.pop()
                    j += 1
        c += len(stack) * 2
                    
        return c

                    
                    
                    

                
        