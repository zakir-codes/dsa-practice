# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ## solution 2: Time O(N), Space(N)
        q = deque([(root.left,root.right)])

        while q:
            l,r = q.popleft()
            if not l and not r:
                continue
            if not l or not r or l.val!=r.val:
                return False
            
            q.append((l.left,r.right))
            q.append((l.right,r.left))
        return True

        # ## solution 1: Time O(N), Space O(H)/O(N)
        # def ismirror(p,q):
        #     if not p and not q:
        #         return True
        #     elif not p or not q or p.val!=q.val:
        #         return False
        #     return ismirror(p.left,q.right) and ismirror(p.right,q.left)
        
        # return ismirror(root.left,root.right)
