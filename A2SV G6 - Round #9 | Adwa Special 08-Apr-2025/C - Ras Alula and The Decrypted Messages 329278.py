# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

for _ in range(int(input())):
    n, m = map(int,input().split())
    s = input()
    w = input()
    sum_ = 0
    sum2 = 0
    for i in w:
        sum_ += ord(i)
    for j in range(m):
        sum2 += ord(s[j])
    l, r = 0, m
    flag = False
    
   
    while r<n:
        if sum2 == sum_:
            flag = True
            break
        sum2 -= ord(s[l])
        sum2 += ord(s[r])
        l += 1
        r += 1
    if sum2 == sum_:
        flag = True
    if flag:
        print('YES')
    else:
        print('NO')


    

    
  
    
    


    
   
  
     
    
