# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(x, y, length):
            check = grid[x][y]
            flag = True
            for i in range(x, x + length):
                for j in range(y, y + length):
                    if grid[i][j] != check:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                return Node(check == 1, True, None, None, None, None)
            half = length // 2
            return Node(True,
                        False,
                        helper(x, y, half),
                        helper(x, y + half, half),
                        helper(x + half, y, half),
                        helper(x + half, y + half, half))
        return helper(0, 0, len(grid))

        