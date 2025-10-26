# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        check = list(set(nums))
        if len(check) < 3:
            return max(nums)
        
        else:
         
            check.sort(reverse = True)
            return check[2]
        

        