# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left = head
        right = head
        n = 0
        while right.next:
            right = right.next
            n += 1

        while left.next != right:
            right.next = left.next
            left.next = right
            
            left = right.next

            curr = right.next
            for i in range(n-2):
                curr = curr.next

            right = curr
            if left == curr:
                left.next = None
                break

            n -= 2

        right.next = None
        # return head