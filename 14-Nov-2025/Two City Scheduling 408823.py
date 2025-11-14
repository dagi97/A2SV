# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = sorted(costs, key = lambda x: x[0] - x[1])
        n = len(costs)
        ans = 0
        for i in range(n//2):
            ans += cost[i][0]
        for i in range(n//2, n):
            ans += cost[i][1]
        return ans

       


      
         



        
            
        