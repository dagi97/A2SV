# Problem: Split Array into Consecutive Subsequences - https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        check = Counter(nums)
        end = defaultdict(int)
       

        for num in nums:
            if check[num]:
                if end[num-1]:
                    end[num-1] -= 1
                    end[num] += 1
                elif check[num + 1] and check[num + 2]:
                    check[num + 1] -= 1
                    check[num + 2] -= 1
                    end[num + 2] += 1

                else:
                    return False
                check[num] -= 1
            
        return True


       
        