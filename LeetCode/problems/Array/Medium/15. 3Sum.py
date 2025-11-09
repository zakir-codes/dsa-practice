class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## solution 1: 3 pointers Time O(N^2) Space O(N^3)
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i-1]==nums[i]:
                continue
            j,k = i+1,n-1
            while j<k:
                num = nums[i] + nums[j]+nums[k]
                if num==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j-1]==nums[j]:
                        j+=1
                    while j<k and nums[k+1]==nums[k]:
                        k-=1
                elif num<0:
                    j+=1
                else:
                    k-=1
        return res
