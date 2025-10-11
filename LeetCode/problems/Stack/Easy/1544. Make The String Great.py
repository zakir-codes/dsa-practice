class Solution:
    def makeGood(self, s: str) -> str:
        ## solution 1
        def clean(string):
            st = []
            for c in string:
                if st and st[-1].lower()==c.lower() and not st[-1]==c:
                    st.pop()
                else:
                    st.append(c)
            return "".join(st)
        return clean(s)
