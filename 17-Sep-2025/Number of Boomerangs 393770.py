# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in points:
            d = {}
            for j in points:
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                dist = dx * dx + dy * dy
                if dist in d:
                    d[dist] += 1
                else:
                    d[dist] = 1
            for v in d.values():
                res += v * (v - 1)
        return res