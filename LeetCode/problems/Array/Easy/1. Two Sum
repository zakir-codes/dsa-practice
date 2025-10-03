class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## solution - 2
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i

        ## solution - 1
        # create postion dict
        # pos = {}
        # for i, n in enumerate(nums):
        #     if n not in pos.keys():
        #         pos[n]=[i]
        #     else:
        #         pos[n].append(i)
        
        # # sort
        # nums = sorted(nums) 
        
        # # 2 pointers and return indices
        # l, r = 0, len(nums)-1
        # while l<r:
        #     if nums[l]+nums[r]<target:
        #         l+=1
        #     elif nums[l]+nums[r]>target:
        #         r-=1
        #     else:
        #         return [pos[nums[r]][-1],pos[nums[l]][0]]
