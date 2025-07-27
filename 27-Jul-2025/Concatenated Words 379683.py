# Problem: Concatenated Words - https://leetcode.com/problems/concatenated-words/

 

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        memo = {}
        
        def can_form(word):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set:
                    if suffix in word_set or can_form(suffix):
                        memo[word] = True
                        return True
            memo[word] = False
            return False

        result = []
        for word in words:
            word_set.remove(word)   
            if can_form(word):
                result.append(word)
            word_set.add(word)   

        return result
