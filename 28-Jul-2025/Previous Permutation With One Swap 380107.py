# Problem: Previous Permutation With One Swap - https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                break
        else:
            return arr

        max_ = -1
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i]:
                if max_ == -1 or arr[j] > arr[max_]:
                    max_ = j
        while max_ > i and arr[max_] == arr[max_ - 1]:
            max_ -= 1

        arr[i], arr[max_] = arr[max_], arr[i]
        return arr
