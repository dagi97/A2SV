# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = 0
        if n < 0:
            flag = 1
            n = -n
        def pow(x,n):

            if n == 0:
                return 1
            if n == 1:
                return x
            
            if n%2 == 0:   
                x *= x         
                return pow(x,n//2)
            else:
                return x * pow(x,n-1)
        if flag:
            return 1/pow(x,n)
        else:
            return pow(x,n)
        