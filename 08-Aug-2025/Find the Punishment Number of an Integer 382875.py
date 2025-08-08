# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s, target):
            if not s:
                return target == 0
            for i in range(1, len(s) + 1):
                if can_partition(s[i:], target - int(s[:i])):
                    return True
            return False
        total = 0
        for i in range(1, n + 1):
            sq = i * i
            if can_partition(str(sq), i):
                total += sq
        return total
