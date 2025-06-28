# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    l,r = 0, 1
    arr.sort()
    flag = True
    while r < n:
        if arr[r]-arr[l] > 1:
            flag = False
        l += 1
        r += 1
    if flag:
        print('YES')
    else:
        print('NO')

