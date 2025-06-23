# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        
        for i in range(len(l)):
            sub = nums[l[i]:r[i]+1]
            sub.sort()
            diff = sub[1] - sub[0]
            is_arithmetic = True
            
            for j in range(1, len(sub)):
                if sub[j] - sub[j-1] != diff:
                    is_arithmetic = False
                    break
                    
            result.append(is_arithmetic)
        
        return result