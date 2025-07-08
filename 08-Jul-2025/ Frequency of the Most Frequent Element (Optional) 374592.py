# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
   
        nums.sort()
        l = 0
        total = 0
        c= 0

        for i in range(len(nums)):
            total += nums[i]

            while (i - l + 1) * nums[i] - total > k:
                total -= nums[l]
                l += 1

            c= max(c, i - l + 1)

        return c

           
     
       


        