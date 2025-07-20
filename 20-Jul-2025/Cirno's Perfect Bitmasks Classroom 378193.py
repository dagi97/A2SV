# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

for _ in range(int(input())):
    n = int(input())
    ans = n & -n
     
   

    while  True:

        if n & ans and ans ^ n:
            print(ans)
            break
           
          
        ans += 1
   
    