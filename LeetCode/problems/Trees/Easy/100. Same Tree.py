# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        ## solution 2: : Time O(N), Space O(H) 
        if not p and not q:
            return True
        elif not p or not q or p.val!=q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        ## solution 1 - time (N) space (N)
        # def travel(node):
        #     if not node:
        #         res.append(None)
        #         return
        #     res.append(node.val)
        #     travel(node.left)
        #     travel(node.right)


        # res = []
        # travel(p)
        # p_l,res = res, []
        # travel(q)
        # return p_l==res
