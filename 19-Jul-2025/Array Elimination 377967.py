# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

from math import gcd
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    check = [0] * 30
    for val in arr:
        for i in range(30):
            if val &(1<<i):
                check[i] += 1
    d = 0
    for i in check:
        d = gcd(d,i)
    ans = []
    for i in range(1, n + 1):
        if d % i == 0:
            ans.append(i)
    print(*ans)
    
