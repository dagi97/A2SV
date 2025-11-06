# Problem: Make Sum Divisible by P - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        
        check = sum(nums)
        rem = check % p
    
        mydict = {0: -1}
        # print(rem)

        if not rem:
            return 0
        
        prefix = 0
        min_ = float('inf')
        
        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p
            x = (prefix - rem + p ) % p

            if x in mydict:
                min_ = min(min_, i- mydict[x])
            mydict[prefix] = i
        
       
        return min_ if min_ < len(nums) else -1
        

        



        
        
     
 
        