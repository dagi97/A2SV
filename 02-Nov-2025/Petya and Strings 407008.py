# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

s = input().lower()
s2 = input().lower()

if s > s2:
    print(1)
elif s2 > s:
    print(-1)
else:
    print(0)