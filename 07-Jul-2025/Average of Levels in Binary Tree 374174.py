# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        out = []
        while queue:
            s = 0
            c = 0
           
            for i in range(len(queue)):
                a = queue.popleft()
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
                s += a.val
                c += 1

            out.append(s/c)
        return out 
                


        