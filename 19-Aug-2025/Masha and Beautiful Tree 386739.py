# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    def merge_sort(arr):
        n = len(arr)

        if n == 1:
            return arr, 0
        mid = n // 2

        left, ls = merge_sort(arr[:mid])
        right , rs = merge_sort(arr[mid:])
        if ls == -1 or rs == -1:
            return [], -1
        merged , swap = merge(left, right)
        if swap == - 1 or ls == -1 or rs == -1:
            return [], - 1
        return merged , swap + ls + rs
    def merge( left , right ):
        if not left or not right:
            return [], -1
        if left[-1] < right[0]:
            return left + right , 0
        elif right[-1] < left[0]:
            return right + left , 1
        else:
            return []  , -1
    _ , res = merge_sort(arr)
    print(res)
        