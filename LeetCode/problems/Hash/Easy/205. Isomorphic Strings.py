class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ## solution 1: Time O(N) Space O(N)
        s_to_t = {}  # Maps characters from s to t
        t_to_s = {}  # Maps characters from t to s
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # Check forward mapping
            if char_s in s_to_t and char_t != s_to_t[char_s]:
                    return False
            else:
                s_to_t[char_s] = char_t
            
            # Check reverse mapping  
            if char_t in t_to_s and char_s != t_to_s[char_t]:
                    return False
            else:
                t_to_s[char_t] = char_s
        
        return True
