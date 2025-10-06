# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        check = [0 for i in range(k)]

        for val in arr:
            check[val % k] += 1

        for i in range(1, k):

            if check[i] != check[k-i]:
                return False
            if i == k - i and check[i] % 2:
                return False
        
        return True
        
        
        

      



   