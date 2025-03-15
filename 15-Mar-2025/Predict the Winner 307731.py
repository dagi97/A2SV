# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def score(l,r):
            if l>r:
                return 0
            sl = nums[l] - score(l+1,r)
             
            sr = nums[r] - score(l,r-1)
            
            return max(sl,sr)
        return score(0,len(nums)-1) >=0
       

        
        