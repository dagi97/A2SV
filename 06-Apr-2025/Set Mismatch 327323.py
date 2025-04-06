# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mydict = Counter(nums)
        for key in mydict:
            if mydict[key] == 2:
                c = key
                break
        n = len(nums)
        s = (n*(n+1))//2
        ans = s+c-(sum(nums))
        return [c,ans]

        