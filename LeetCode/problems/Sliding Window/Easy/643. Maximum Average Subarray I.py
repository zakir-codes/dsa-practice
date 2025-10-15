class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ## solution 2
        s = sum(nums[:k])
        max_avg = s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            max_avg = max(max_avg, s)
        return max_avg/k
        
        
        # ## solution 1
        # max_avg = -1000000
        # s = 0
        # for i in range(len(nums)):
        #     s+=nums[i]

        #     if i>=k:
        #         s-=nums[i-k]
        #     if i>=k-1:
        #         max_avg = max(max_avg, s)
        # return max_avg/k
