class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1,n2 = len(nums1),len(nums2)
        # sort
        nums1.sort()
        # search history
        set_p = set()
        out = []
        # binany search and store value for each value
        for n in nums2:
            if not n in set_p:
                l,r=0,n1-1
                while l<=r:
                    mid=(l+r)//2
                    if nums1[mid]==n:
                        out.append(n)
                        break
                    elif nums1[mid]<n:
                        l = mid+1
                    else:
                        r = mid-1
                set_p.add(n)
        return out
