class Solution:
    def mySqrt(self, x: int) -> int:
        ## solution 1
        if x<2:
            return x
        
        l,r = 2,x
        while l<=r:
            mid=(l+r)//2
            sq = mid**2
            if x == sq:
                return mid
            elif sq<x:
                l=mid+1
            else:
                r = mid-1
        return r
