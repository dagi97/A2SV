# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        check = []

        def back(node):
            nonlocal check
            if not node:
                return 
            back(node.left)
            check.append(node.val)
            back(node.right)

        def build(check):

            if not check:
                return 
            
            mid = len(check)//2
            root = TreeNode(check[mid])
            root.right = build(check[mid + 1:])
            root.left = build(check[:mid])

            return root 
        back(root)

        return build(check)


            
            
        


        