class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ## solution 1: Time O(N), Spcae O(1)
        ptr_t, n_t = 0, len(t)
        ptr_s, n_s = 0, len(s)
        while ptr_t<n_t and ptr_s<n_s:
            if s[ptr_s]==t[ptr_t]:
                ptr_s+=1
            ptr_t+=1
        return ptr_s==n_s
