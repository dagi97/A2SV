# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
    
        check = '0123456789'
        for i in range(n):
            if s[i] != ']':
                stack.append(s[i])
            else:
                c =''
                while stack[-1] != '[':
                    c = stack.pop() + c
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*c)
        return ''.join(stack)
        

                
                    
            


            
        