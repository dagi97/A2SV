# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isValid(mid):
            n = len(nums)
            check = [0] * (n+1)
            
            for i in range(mid):
               l, r, val = queries[i]
               check[l] -= val
               check[r+ 1] += val

            for i in range(1, n):
                check[i] += check[i-1]
            
            for i in range(n):
                if nums[i] + check[i] > 0:
                    return False
            return True

        low = 0
        high = len(queries)
        while low <= high:
            mid = (low + high) // 2
           
            if isValid(mid):
                high = mid - 1
            else:
                low = mid + 1
        if low == len(queries) + 1 and not isValid(mid):
            return -1
        return low
            
        

        