class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ## solution 1: Time O(N^2) Space O(N^2) -O(N*(N+1)/2)
        res = []
        for l in range(numRows):
            l_res = []
            for i in range(l+1):
                if i==0 or i==l:
                    l_res.append(1)
                else:
                    l_res.append(res[-1][i-1]+res[-1][i])
            res.append(l_res)
        return res
