# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def isValid(h):
            c = 0
            for i in citations:
                if i >= h:
                    c += 1
            return c >= h
            
        
        
        low = 1
        high = len(citations) 
        while low <= high:
            mid = ( low + high ) //2
            if isValid(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high

         
        