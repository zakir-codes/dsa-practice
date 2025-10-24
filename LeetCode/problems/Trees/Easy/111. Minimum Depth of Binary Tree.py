# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ## solution 1: BFS: Time O(N), Space O(W)
        ## edge case [none]
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        while queue:
            level_size = len(queue)
            depth+=1
            for _ in range(level_size):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

