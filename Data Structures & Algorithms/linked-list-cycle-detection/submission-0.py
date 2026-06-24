# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rec = set()
        ptr = dummy = ListNode(0, head)
        while ptr.next is not None:
            if ptr.next in rec:
                return True
            rec.add(ptr.next)
            ptr = ptr.next
        return False