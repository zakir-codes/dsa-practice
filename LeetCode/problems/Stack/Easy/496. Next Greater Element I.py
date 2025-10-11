class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ## solution 2
        map_nge = {}
        st = []
        for n in nums2:
            while st and n>st[-1]:
                map_nge[st.pop()] = n
            st.append(n)

        st = []
        for n in nums1:
            st.append(map_nge.get(n,-1))
        return st

        ## solution 1
        # st = []
        # map_g = {}
        # for n in nums2:
        #     for i in range(len(st)-1,-1,-1):
        #         if st[i]<n:
        #             map_g[st[i]] = n
        #             st.pop(i)
        #     st.append(n)
        # st = []
        # for n in nums1:
        #     st.append(map_g.get(n,-1))
        # return st
