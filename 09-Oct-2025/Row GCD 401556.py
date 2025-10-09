# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

import math
n, k = map(int, input().split())
a = list( map(int, input().split()))
b = list( map(int, input().split()))
check = 0

for i in a:
    check = math.gcd(check, abs(i-a[0]))

ans = []

for j in b:
    curr = math.gcd(a[0] + j, check)
    ans.append(curr)
print(*ans)