# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        c = 0
        def helper(root):
            nonlocal c
            if not root:
                return (0,0)
            
            left_ , leftc = helper(root.left)
            right_ , rightc = helper(root.right)

            total = left_ + right_ + root.val
            cnt = leftc + rightc + 1

            if total//cnt == root.val:
                c += 1
            return(total,cnt )
        helper(root)
        return c

        
        