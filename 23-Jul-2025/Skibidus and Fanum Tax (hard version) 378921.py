# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    def isValid(mid,i):
        if i == 0:
            return True
        elif a[i-1] <= b[mid] -a[i]:
            return True
        else:
            return False

    for i in range(n):
        l,h = 0, k-1
        ans = -1

        while l <= h:
            mid = (l + h) // 2
            if isValid(mid, i):
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        if ans == -1:
            continue
        if i != 0 and a[i-1] <= a[i]:
            res = min(b[ans]-a[i],a[i])
        elif i == 0:
            res = min(b[ans]-a[i],a[i])
        else:
            res = b[ans] - a[i]

        a[i] = res 
                
    if a == sorted(a):
        print('YES')
    else:
        print('NO')



