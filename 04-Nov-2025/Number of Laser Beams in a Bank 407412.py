# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        check = 0
        ans = 0

        for i in bank:

            c = i.count('1')
            if c and check:
                ans +=  c * check
            if c:
                check = c
        return ans
           
       
       
       

  