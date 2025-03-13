# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def change(s):
            s = list(s)
            for i in range(len(s)):
                if s[i] == '0':
                    s[i] = '1'
                else:
                    s[i] = '0'
            c = s[::-1]
            return ''.join(c)
        self.s = '0'
        def bit(n):
            if n == 1:
                return self.s
            self.s =  self.s + '1' + change(self.s)  
            return bit(n-1)
        
        check = bit(n)
        return check[k-1]
            
            
            

        