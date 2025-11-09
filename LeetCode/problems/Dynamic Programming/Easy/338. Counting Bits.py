class Solution:
    def countBits(self, n: int) -> List[int]:
        ## solution 1: Time O(N) Space O(N)
        ans = [0]*(n+1)
        for i in range(n+1):
            ans[i] = ans[i//2]+1 if i%2!=0 else ans[i//2]
        return ans
