# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = []
        while head:
            check.append(head.val)
            head = head.next
        check.sort()
        dummy = ListNode()
        curr = dummy
        for i in range(len(check)):
            curr.next = ListNode(check[i])
            curr = curr.next
        return dummy.next
        