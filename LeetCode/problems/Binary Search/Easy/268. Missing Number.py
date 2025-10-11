class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## solution 4: space O(1), time O(N)
        # n = len(nums)
        # return (n*(n+1))//2 - sum(nums)
        
        ## solution 3:
        nums.sort()

        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==mid:
                l = mid+1
            elif nums[mid]>mid:
                r = mid-1
        return l



        ## solution 2: space O(1), time O(N LogN)
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i-1]+1!=nums[i]:
        #         return nums[i-1]+1
        # return len(nums) if len(nums)!=nums[-1] else 0
        ## solution 1: space O(N), Time O(N)
        # return list(set(range(len(nums)+1))-set(nums))[0]
