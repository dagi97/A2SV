# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    arr = list(map(int, input().split()))

    def isvalid(mid):
        a = "R"
        c = 0
        for i in range(n):
            if arr[i] > mid:
                if s[i] == "B" and a == "R":
                    c += 1
                a = s[i]
        return c <= k
    low = 0
    high = max(arr)

    while low <= high:
            mid = (low+high) // 2
            if isvalid(mid):
                high = mid-1
            else:
                low = mid + 1
    print(low)
    