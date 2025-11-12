# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        check = n // 2
        a = pow(4 , check,MOD) * pow(5 ,check,MOD)

        if n % 2:
            a *= pow(5, n % 2, MOD)

         
        return a % MOD


 
            
          


         
        
        