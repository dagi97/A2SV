# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def check(node,min_,max_):
            if not node:
                return
            minn = min(node.val, min_)
            maxx = max(node.val, max_)

            self.ans = max(self.ans, maxx - minn)

            check(node.left, minn, maxx)
            check(node.right, minn, maxx)
        check(root,root.val,root.val)
        return self.ans
            