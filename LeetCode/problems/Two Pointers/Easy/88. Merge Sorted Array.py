class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## solution 1
        r_m = m-1
        r_n = n-1
        r_i = m+n-1

        while r_n>=0 and r_m>=0:
            if nums1[r_m]<=nums2[r_n] or nums1[r_m]==None:
                nums1[r_i] = nums2[r_n]
                r_n-=1
            else:
                nums1[r_i] = nums1[r_m]
                nums1[r_m]=None
                r_m-=1
            r_i-=1
        if r_m<0 and r_n>-1:
            nums1[:r_n+1]=nums2[:r_n+1]
