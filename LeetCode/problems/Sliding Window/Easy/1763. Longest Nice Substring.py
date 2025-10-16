class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ## solution 2
        for i, c in enumerate(s):
            if not c.swapcase() in s:
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        return s
        
        # ## solution 1
        # ss = set(s)
        # for i, c in enumerate(s):
        #     if not c.swapcase() in ss:
        #         s0 = self.longestNiceSubstring(s[:i])
        #         s1 = self.longestNiceSubstring(s[i+1:])
        #         return max(s0, s1, key=len)
        # return s
        
        
