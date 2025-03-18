# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        flag = True
        queue = deque([root])
        while queue:
            c = len(queue)
            ans = []
            for _ in range(c):
                check = queue.popleft()
                if check.left:
                    queue.append(check.left)
                if check.right:
                    queue.append(check.right)
                ans.append(check.val)
              
            if flag:
                res.append(ans)
                flag = False
            else:
                ans = ans[::-1]
                res.append(ans)
                flag = True
        return res
                

        

        