class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        ## solution 1:
        def clean(string):
            st = []
            for c in string:
                if c=="#" and st:
                    st.pop()
                elif c!="#":
                    st.append(c)
            return st
        
        return clean(s)==clean(t)
