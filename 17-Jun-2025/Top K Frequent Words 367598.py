# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        check = Counter(words)
        sorted_check =sorted(check.items(), key = lambda x :( -x[1], x[0]))
        return [key for key,  val in sorted_check[:k]]


        