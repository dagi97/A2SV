# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        check = Counter(arr)
        l = sorted(check.values())
        n = len(arr) // 2
        k = 0
        c = 0
        i = len(l) - 1
        while k < n:
            k += l[i]
            c += 1
            i -= 1
        return c
