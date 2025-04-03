# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
nums = list(map(int,input().split()))
s, d = 0, 0
l,r = 0 , n-1
flag = True
while l<=r:
    if nums[l] < nums[r] and flag:
        s += nums[r]
        r -= 1
        flag = False
    elif nums[l] >= nums[r] and flag:
        s += nums[l]
        l += 1
        flag = False
    elif nums[l] < nums[r] and not  flag:
        d += nums[r]
        r -= 1
        flag = True
    elif nums[l] >= nums[r] and not flag:
        d += nums[l]
        l += 1
        flag = True
print(s,d)

