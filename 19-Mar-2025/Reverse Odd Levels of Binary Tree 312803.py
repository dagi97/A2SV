# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        c = 0 
        
        while queue:
            n = len(queue)
            if c%2:
                l, r = 0, n-1
                while l<r:
                    queue[l].val, queue[r].val = queue[r].val, queue[l].val
                    l += 1
                    r -= 1
            for _ in range(n):
                check = queue.popleft()
                if check.left:
                    queue.append(check.left)
                if check.right:
                    queue.append(check.right)
            c += 1
       
        return root
        
            






        