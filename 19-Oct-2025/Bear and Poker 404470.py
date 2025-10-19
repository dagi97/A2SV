# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    while not arr[i] % 2 or not arr[i] % 3:
        if not arr[i] % 2:
            arr[i] //= 2
        if not arr[i] % 3:
            arr[i] //= 3
if len(set(arr)) == 1:
    print('Yes')
else:
    print('No')