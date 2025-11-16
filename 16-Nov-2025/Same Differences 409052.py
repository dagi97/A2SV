# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    check = defaultdict(int)
    c = 0
    for i, val in enumerate(arr):
        c += check[val - i]
        check[val - i] += 1

    print(c)
        
