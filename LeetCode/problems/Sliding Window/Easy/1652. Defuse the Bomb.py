class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        ## solution 1
        n = len(code)
        out = [0]*n
        if k==0:
            return out

        for i in range(n):
            s_cur = 0
            if k>0:
                for j in range(1,1+k):
                    s_cur += code[(i+j)%n]
            else:
                for j in range(1,1+abs(k)):
                    s_cur += code[(i-j)%n]
            out[i] = s_cur
        return out
