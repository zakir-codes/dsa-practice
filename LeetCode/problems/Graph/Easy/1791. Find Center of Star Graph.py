class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # ## solution 2: Time O(1), Space O(1)
        # # edge case: covered
        # # business logic: 1. center appears in every edge

        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1] 
        # ## solution 1: Time O(N), Space O(N)
        # # edge case - covered
        # # business logic - 1. count n-1
        # n = len(edges)
        # edge_count = [0]*(2+n)

        # for u,v in edges:
        #     edge_count[v]+=1
        #     edge_count[u]+=1
        
        # return edge_count.index(n)
