# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ## solution 2 - time O(N), space O(1)
        dummy = ListNode(0, head)

        cur = dummy
        while cur.next:
            if cur.next.val ==val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

        ## solution 1 - time O(N), space O(1)
        # edge cases [] 1; [7,7] 7; 
        
        # while head and head.val == val: # [7,7] 7;
        #     head = head.next
        # if not head: # [] 1;
        #     return head

        # prev, cur = head, head.next
        # while cur:
        #     while cur and cur.val == val:
        #         cur = cur.next
        #     prev.next = cur 
        #     prev = cur
        #     cur = cur.next if cur else None
        # return head
