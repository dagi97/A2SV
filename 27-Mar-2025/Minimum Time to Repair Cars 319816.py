# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
      
        def isValid(mid):
            check = 0
            for i in ranks:
                n = int(sqrt(mid/i))
                check += n
             
                
            return  check >= cars
                 



        high = min(ranks) * (cars**2)
        low = min(ranks)
        while low <= high:
            mid = (low+high)//2
            if isValid(mid):
                high = mid -1
            else:
                low = mid + 1
        return low

        