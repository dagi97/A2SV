# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
def prime_factors(n):
    div = 2
    c = 0
    while div * div <= n:
        if n % div == 0:
            c += 1
            while n % div == 0:
                n //= div
        div += 1
    if n > 1:
        c += 1
            
    return c
ans = 0
while n:
    if prime_factors(n) == 2:
        ans += 1
    n -= 1
    

print(ans)