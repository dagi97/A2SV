# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root,val):
            if not root:
                return
            val *= 10
            val += root.val
            if not root.right and not root.left:
              self.res += val
              return
            dfs(root.left,val)
            dfs(root.right,val)
        dfs(root,0)
        return self.res
    

        