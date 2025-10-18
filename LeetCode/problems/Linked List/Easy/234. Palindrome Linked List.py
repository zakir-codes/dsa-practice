# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ## solution 2 - time O(N) space O(1)
        def reverse(node):
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next # Middle or start of second half
            fast = fast.next.next

        head_rev = reverse(slow)

        while head_rev:
            if head_rev.val!=head.val:
                return False

            head_rev = head_rev.next
            head = head.next
        
        return True
        
        # ## solution - 1 time O(N) space O(N)         
        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next # Middle or start of second half
        #     fast = fast.next.next
        
        # start = head
        # l,r = [], []
        # while slow:
        #     l.append(start.val)
        #     r.append(slow.val)
            
        #     slow = slow.next
        #     start = start.next
        # return True if l[::-1]==r else False
