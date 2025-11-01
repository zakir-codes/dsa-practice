class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # solution 2: iterative DFS Space O(N), Time(N)
        if source==destination:
            return True
        
        # graph to dict
        paths = {}
        for u,v in edges:
            if u not in paths:
                paths[u] = set()
            if v not in paths:
                paths[v] = set()
            paths[u].add(v)
            paths[v].add(u)
        
        # Iterative DFS
        visited = set([source])
        stack = [source]
        while stack:
            q = stack.pop()
            if q==destination:
                return True
            for n in paths[q]:
                if not n in visited:
                    visited.add(n)
                    stack.append(n)
        return False

        # solution 1: recursive DFS Space O(N), Time(N)
        # edge cases: n=1;
        # if source==destination:
        #     return True

        # paths = {}
        # for u,v in edges:
        #     if u not in paths:
        #         paths[u] = set()
        #     if v not in paths:
        #         paths[v] = set()
        #     paths[u].add(v)
        #     paths[v].add(u)
        
        # visited = set([source])
        # def dfs(node):
        #     if destination in paths.get(node,[]):
        #         return True

        #     for p in paths.get(node,[]):
        #         if not p in visited:
        #             visited.add(p)
        #             if dfs(p):
        #                 return True
        #     return False
        # return dfs(source)
