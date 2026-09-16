# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # # edge cases where either list is empty
        # if not list1:
        #     return list2
        # elif not list2:
        #     return list1


        c1, c2 = list1, list2

        new = ListNode()
        curr = new

        while c1 and c2:
            if c1.val < c2.val:
                curr.next = ListNode(c1.val)
                curr = curr.next
                c1 = c1.next

            else:
                curr.next = ListNode(c2.val)
                curr = curr.next
                c2 = c2.next

        if c1:
            curr.next = c1
        
        elif c2:
            curr.next = c2

        return new.next
