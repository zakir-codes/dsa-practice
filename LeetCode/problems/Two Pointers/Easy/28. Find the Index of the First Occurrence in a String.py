class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ## solution 2
        n_nee, n_hay = len(needle),len(haystack)
    
        if n_nee>n_hay:
            return -1
        
        l=0
        while l+n_nee<=n_hay:
            if haystack[l:l+n_nee]==needle:
                return l
            l+=1
        return -1
        
        ## solution 1
        # return haystack.find(needle)
