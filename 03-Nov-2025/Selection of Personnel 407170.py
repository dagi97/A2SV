# Problem: Selection of Personnel - https://codeforces.com/problemset/problem/630/F

from math import comb

n = int(input())
ans = comb(n, 5) + comb(n, 6) + comb(n, 7)
print(ans)