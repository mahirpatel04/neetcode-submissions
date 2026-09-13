# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        further = head
        for i in range(n):
            further = further.next

        if further == None:
            return head.next

        curr = head
        while further and further.next:
            curr = curr.next
            further = further.next

        
        curr.next = curr.next.next
        return head
        

        