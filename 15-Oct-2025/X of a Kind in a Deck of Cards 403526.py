# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dict = Counter(deck)
        from math import gcd
        def solve(nums):
            if len(nums) == 1:
                return nums[0]

            div = gcd(nums[0], nums[1])

            if len(nums) == 2:
                return div

            for i in range(1, len(nums) - 1):
                div = gcd(div, nums[i + 1])
                if div == 1:
                    return div
            return div

        hcf = solve(list(dict.values()))

        if hcf > 1: return True
        else: return False