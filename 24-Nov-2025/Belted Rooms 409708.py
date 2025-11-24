# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = set()
    if "<" not in s or ">" not in s:
        print(n)
    else:
        for i in range(n):
            if s[i] == '-':
                ans.add(i)
                ans.add((i + 1) % n)
        print(len(ans))
