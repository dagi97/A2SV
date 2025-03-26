# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zeros = arr.count(0)
        
        i = n - 1
        while i >= 0:
            if arr[i] == 0:
                if i + zeros < n:
                    arr[i + zeros] = 0
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
            else:
                if i + zeros < n:
                    arr[i + zeros] = arr[i]
            i -= 1
