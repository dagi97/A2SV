# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:

        isprime = [True for i in range(n)]
        d = 2
        if n > 0:
            isprime[0] = False
        if n > 1:
            isprime[1] = False
        while d * d < n:
            if isprime[d]:
                j = d * d
                while j < n:
                    isprime[j] = False
                    j += d
            d += 1
        return isprime.count(True)


           


        