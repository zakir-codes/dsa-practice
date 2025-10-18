# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## solution 1 - Time O(N), Space - O(1)
        if not head:
            return head
        prev, cur, nex = None, head, head.next

        while nex: # recheck
            cur.next = prev
            prev = cur
            cur = nex
            nex = nex.next
        cur.next = prev

        return cur


