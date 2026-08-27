# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        if not head.next:
            return head

        stack = []
        while head != None:
            stack.append(head.val)
            head = head.next

        root = ListNode(stack.pop())
        curr = root
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next

        return root
