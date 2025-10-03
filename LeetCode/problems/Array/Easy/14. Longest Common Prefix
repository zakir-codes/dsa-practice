class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ## solution - 2
        lcp = strs[0]
        n_lcp = len(lcp)

        for s in strs[1:]:
            while lcp[:n_lcp]!=s[:n_lcp]:
                n_lcp-=1
                if n_lcp==0:
                    return ""
            lcp = lcp[:n_lcp]
        return lcp

        ## solution - 1
        # out = strs[0]
        # for s in strs:
        #     # if anythign is empty or cur str length is less than out
        #     if out=="" or s=="":
        #         return ""
        #     if len(out)>len(s):
        #         out = out[:len(s)]
        #     # check str one ele at a time
        #     for i in range(len(out)-1,-1,-1):
        #         if s[i]!=out[i]:
        #             out = out[:i]
        # return out
