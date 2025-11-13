# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        diff = abs(startPos - endPos)
        check = k - diff
        MOD = 10**9 + 7

        if diff > k or check % 2:
            return 0
        
        check //= 2

        return math.comb(k, check) % MOD
