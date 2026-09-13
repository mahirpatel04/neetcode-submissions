# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # set a pointer N nodes down head
        further = head
        for i in range(n):
            further = further.next

        # create a second pointer at head and keep iterating till the further one gets to the end
        # this will give us a pointer to the node that is N away from the end
        curr = dummy
        while further:
            curr = curr.next
            further = further.next

        # relink and return
        curr.next = curr.next.next
        return dummy.next
        

        