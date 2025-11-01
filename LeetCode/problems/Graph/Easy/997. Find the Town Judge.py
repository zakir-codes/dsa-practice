class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ## solution 1: Space O(N), Time O(N)
        # edge case (1, [])
        if n==1:
            return 1

        trust_count = [0]*(n+1)
        trust_others = [0]*(n+1)

        for a,b in trust:
            trust_others[a]+=1
            trust_count[b]+=1
        for p in range(1,n+1):
            if trust_count[p]==n-1 and trust_others[p]==0:
                return p
        return -1
                
