# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        further = head
        for i in range(n):
            further = further.next


        curr = dummy
        while further:
            curr = curr.next
            further = further.next

        curr.next = curr.next.next
        return dummy.next
        

        