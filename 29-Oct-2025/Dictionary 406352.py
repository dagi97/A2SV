# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

for i in range(int(input())):
    s = input()
 
    a = ord(s[0]) - 97
 
    b = ord(s[1]) - 97
 
    if a > b:
        b += 1
    
   
    print((25 * a) + b)