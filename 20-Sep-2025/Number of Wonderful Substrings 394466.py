# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = {0: 1}
        mask = 0
        res = 0
        for ch in word:
            mask ^= 1 << (ord(ch) - ord('a'))
            res += count.get(mask, 0)
            for i in range(10):
                res += count.get(mask ^ (1 << i), 0)
            count[mask] = count.get(mask, 0) + 1
        return res
