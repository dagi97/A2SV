# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a == b:
        print(-1)
    else:
        print((1 << 30) - max(a, b))