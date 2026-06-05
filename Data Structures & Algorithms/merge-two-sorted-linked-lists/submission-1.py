# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # iterative method: good space complexity
        # dummy = ptr = ListNode() # ptr is the worker, taking node from List1 and List2. dummy is for locate the head of list
        # while list1 and list2:
        #     if list1.val >= list2.val:
        #         ptr.next = list2
        #         list2 = list2.next
        #     else:
        #         ptr.next = list1
        #         list1 = list1.next
        #     ptr = ptr.next
        # ptr.next = list1 or list2
        # return dummy.next
        if list1 is None:
            return list2
        if list2 is None: 
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        




