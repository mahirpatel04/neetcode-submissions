# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # set a pointer N nodes down head
        further = head
        for i in range(n):
            further = further.next

        # if there's no node N nodes down that means we want to remove head (just return head.next)
        if further == None:
            return head.next

        # create a second pointer at head and keep iterating till the further one gets to the end
        # this will give us a pointer to the node that is N away from the end
        curr = head
        while further and further.next:
            curr = curr.next
            further = further.next

        # relink and return
        curr.next = curr.next.next
        return head
        

        