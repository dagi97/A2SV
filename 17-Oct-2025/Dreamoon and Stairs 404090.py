# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

import math

n, m = map(int, input().split())

min_, max_ = math.ceil(n/2), n
valid = False
for i in range(min_, max_ + 1):
    if not i % m:
        print(i)
        valid = True
        break
if not valid:print(-1)
    

