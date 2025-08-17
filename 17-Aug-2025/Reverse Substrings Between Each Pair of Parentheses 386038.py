# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i== ")":
                b = ""
                while True:
                    a = stack.pop()
                    if a== "(":
                        break
                    b += a[::-1]
                stack.append(b)
            
                    
            else:
                stack.append(i)
        print(stack)
        return "".join(stack)

                    
        