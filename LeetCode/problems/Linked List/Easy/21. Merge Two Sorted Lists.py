# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ## solution 2 - time O(N1 + N2); space O(1)
        head = ListNode(0)
        dummy = head

        while list1 and list2:
            if list1.val<=list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        
        head.next = list1 or list2
        return dummy.next
        
        ## solution 1 - time O(N1 + N2); space O(1)
        # # edge case
        # if not list1 and not list2:
        #     return list1
        # elif not list1:
        #     return list2
        # elif not list2:
        #     return list1
        
        # head = ListNode(0)
        # dummy = head
        # while list1 and list2:
        #     if list1.val<=list2.val:
        #         head.next = list1
        #         list1 = list1.next
        #     else:
        #         head.next = list2
        #         list2 = list2.next
        #     head = head.next
        # head.next = list2 if not list1 else list1
        
        # return dummy.next
