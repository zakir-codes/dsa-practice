class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # new alphabet - set
        # diff freq - sorted, dict
        
        ## solution 2
        if len(s)!=len(t):
            return False

        s_dict = {}
        for a in s:
            s_dict[a] = s_dict.get(a,0)+1

        t_dict = {}
        for a in t:
            # if a not in s_dict:
                # return False
            t_dict[a] = t_dict.get(a,0)+1

        if t_dict==s_dict:
            return True
        return False

        ## solution 1
        # if sorted(s)==sorted(t):
        #     return True
        # return False
