# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## solution 3: without [::-1] stack Time O(N), O(N)
        
        ## solution 2: stack Time O(N), O(N)
        if not root:
            return []
        stack = [root]
        res =[]
        while stack:
            n = stack.pop()
            res.append(n.val)
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
            
        return res[::-1]


        ## solution 1: helper function Time O(N), O(N)
        # res = []
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     dfs(node.right)
        #     res.append(node.val)
        
        # dfs(root)
        # return res
