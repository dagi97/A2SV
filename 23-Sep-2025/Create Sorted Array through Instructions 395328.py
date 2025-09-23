# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        MOD = 10**9 + 7
        arr, cost = [], 0
        for x in instructions:
            left = bisect_left(arr, x)
            right = len(arr) - bisect_right(arr, x)
            cost = (cost + min(left, right)) % MOD
            insort(arr, x)
        return cost
