# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

import math
for _ in range(int(input())):
    l,r, d = map(int, input().split())
    a = math.ceil(l/d) - 1
    b = math.ceil(r/d)

    if a > 0:
        print(d)
    elif not r % d:
        print((b + 1) *d)
    else:
        print(b * d)
