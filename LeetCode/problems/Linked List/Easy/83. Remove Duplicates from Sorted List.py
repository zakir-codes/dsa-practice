# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## solution 1 - time O(N) space O(1)
        
        # edge cases [], already sorted, [1]
        if not head: # []
            return head
        
        prev, cur = head, head.next
        while cur: 
            while cur and prev.val==cur.val:
                prev.next = cur.next
                cur = cur.next
            prev = cur
            cur = cur.next if cur else None
        return head
