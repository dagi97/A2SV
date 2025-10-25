# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        check = set()
        for i in range(len(boxes)):
            if boxes[i] == '1':
                check.add(i)
        ans = []
        for j in range(len(boxes)):

            c = 0

            for i in check:
                c += abs(j - i)
            ans.append(c)
        return ans
        