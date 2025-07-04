# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True

        if len(flowerbed) > 1:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1  
                c += 1
        
        for i in range(1, len(flowerbed)):
            if flowerbed[i-1]  == 1:
                continue
            if i + 1 < len(flowerbed) and flowerbed[i+1] ==1:
                continue
            if flowerbed[i] == 0:
                flowerbed[i] = 1
                c += 1
        return c >= n
            

   
            
        


        