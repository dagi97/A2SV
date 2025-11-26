# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h=len(citations)
        citations.sort()
        for i in range(len(citations)):

            if citations[i] < h:
                h-=1
            else:
                break
        return h
        