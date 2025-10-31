# Problem: k-Factorization - https://codeforces.com/problemset/problem/797/A

import math
n, k = map(int, input().split())

def prime_factorization(n):
    fact = []
    while not n % 2:
        fact.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while not n % i:
            n //= i
            fact.append(i)
    if n > 2:
        fact.append(n)
    return fact
fact = prime_factorization(n)
 

if len(fact) < k:
    print(-1)
elif len(fact) == k:
    print(*fact)
else:
    num = 1
    diff = len(fact) - k
    for i in range(diff + 1):
        num *= fact[i]
    num = [num]
    num.extend(fact[diff + 1:])

    print(*num)



            


