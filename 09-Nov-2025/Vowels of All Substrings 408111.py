# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowel = {'a','e','i','o','u'}
        c = 0

        for i, val in enumerate(word):
            if val in vowel:
                c += (n-i) * (i + 1)
        return c

        