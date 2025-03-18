# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            max_ = queue[0].val
            c = len(queue)
            for _ in range(c):
                check = queue.popleft()
                max_ = max(max_ , check.val)
                if check.left:
                    queue.append(check.left)
                if check.right:
                    queue.append(check.right)
            res.append(max_)
        return res
           
        