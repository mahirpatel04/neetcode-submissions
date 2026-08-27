# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptrs = set()

        while head:
            print(ptrs)
            if head in ptrs:
                return True
            
            else:
                ptrs.add(head)
                head = head.next
        
        return False