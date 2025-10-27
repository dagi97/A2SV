# Problem: Reducing Dishes - https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n  = len(satisfaction)
        satisfaction.sort()
        res  = 0
        sum_ = 0
      

        for i in range(n-1, -1, -1):
            val = satisfaction[i]
            if val + sum_ > 0:
                sum_ += val
                res += sum_
            else:
                break
        return res

      

            

        
        