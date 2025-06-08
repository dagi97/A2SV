# Problem: Maximum Element After Decreasing and Rearranging - https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        l, r = 0, 1
        c = 0
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] +1
            c = max(arr[i],c)
        return max(c, arr[-1])
        

        