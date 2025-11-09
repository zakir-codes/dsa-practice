class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## solution 1: Greedy Time O(N), Space O(1)
        vol = 0
        l,r = 0, len(height)-1
        while l<r:
            vol = max(vol, min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return vol
