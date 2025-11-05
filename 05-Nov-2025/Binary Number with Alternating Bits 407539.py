# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)
        for i in range(2, len(s)):
            if s[i] == s[i-1]:
                return False
        return True
        