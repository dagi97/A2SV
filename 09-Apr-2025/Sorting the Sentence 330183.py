# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        k = list(s.split())
        k.sort(key = lambda x:x[-1])
        for i in range(len(k)):
            n = len(k[i])
            k[i] =k[i][:n-1]
        
         
        return " ".join(k)
        