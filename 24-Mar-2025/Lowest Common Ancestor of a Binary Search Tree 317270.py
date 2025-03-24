# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(root):
            if max(p.val,q.val) > root.val and min(p.val,q.val) < root.val:
                return root
            if root.val == q.val or root.val == p.val:
                return root
            while root:
                if root.val < q.val:
                    return LCA(root.right)
                else:
                    return LCA(root.left)
        return LCA(root)

            
           
      