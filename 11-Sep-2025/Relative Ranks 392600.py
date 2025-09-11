# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = list(zip(score, range(len(score))))
        score.sort(reverse = True)
        ans = [0] * len(score)
        c = 1

        for val, ind in score:
            if c == 1:
                ans[ind] = "Gold Medal"
            elif c == 2:
                ans[ind] = "Silver Medal"
            elif c == 3:
                ans[ind] = "Bronze Medal"
            else:
                ans[ind] = str(c)
            c += 1
        return ans



            
        