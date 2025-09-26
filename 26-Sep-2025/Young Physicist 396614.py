# Problem: Young Physicist - https://codeforces.com/problemset/problem/69/A

n=int(input())
x , y, z=0 , 0, 0


for i in range(n):
    k = list(map(int,input().split()))
    x += k[0]
    y += k[1]
    z += k[2]
  
if y == z == x == 0:
    print("YES")
else:
    print("NO")