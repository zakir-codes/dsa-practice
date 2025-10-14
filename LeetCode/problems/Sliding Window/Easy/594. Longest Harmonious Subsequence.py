class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ## solution 1
        h_count = {}
        max_s = 0
        for n in nums:
            h_count[n] = h_count.get(n,0) + 1
        
        for x in h_count:
            x_1 = x+1
            if x_1 in h_count:
                c = h_count[x]+ h_count[x_1]
                max_s = max(max_s, c)
        return max_s
