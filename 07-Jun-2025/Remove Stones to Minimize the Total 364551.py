# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        
        for i in piles:
            heappush(heap, -i)

        while k:
            j = -heappop(heap)
            diff = j // 2
            j -= diff
            if j > 0:
                heappush(heap, -j)
            k -= 1
            
        return -sum(heap) 
            



        