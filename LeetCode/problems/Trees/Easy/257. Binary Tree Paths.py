# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ## solution 2: DFS; better O(N), Space O(H)
        res = []
        def dfs(node, path):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append("->".join(path))
            else:
                dfs(node.left,path)
                dfs(node.right,path)
            
            path.pop()
        dfs(root, [])

        return res
        
        ## solution 1: BFS Time O(N), Space O(W)× O(H)
        # q = deque([(root,"")])
        # out = []
        # while q:
        #     l_size = len(q)
        #     for _ in range(l_size):
        #         node, s = q.popleft()
        #         s=s+"->"+str(node.val)
        #         if not node.left and not node.right:
        #             out.append(s[2:])
        #         if node.left:
        #             q.append((node.left,s))
        #         if node.right:
        #             q.append((node.right,s))
        # return out
        
