# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        c = 0
        def help(node):
            nonlocal c
            if not node:
                return 
            help(node.right)
            node.val += c
            c = node.val
            help(node.left)
        help(root)
        return root

        
        