# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        c = max(candies)
        ans = []
        for i in candies:
            if i + extraCandies >= c:
                ans.append(True)
            else:
                ans.append(False)
        return ans