# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        ans = [0] * n
        
        availabel, occupied = list(range(n)), []
        for i in range(n):
            times[i].append(i)
        times.sort()
        for u,v, i in times:
            while occupied and occupied[0][0] <= u:
                _ , free = heappop(occupied)
                heappush(availabel, free)
            b = heappop(availabel)
            ans[i] =  b
            heappush(occupied, [v,b])
        return ans[targetFriend]

    
        
        