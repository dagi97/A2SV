# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
       
            minutes = []
            for time in timePoints:
                h, m = map(int, time.split(":"))
                total = h * 60 + m
                minutes.append(total)

            minutes.sort()

            min_diff = float('inf')
            for i in range(1, len(minutes)):
                diff = minutes[i] - minutes[i - 1]
                min_diff = min(min_diff, diff)

            wrap_diff = 1440 + minutes[0] - minutes[-1]
            min_diff = min(min_diff, wrap_diff)

            return min_diff
