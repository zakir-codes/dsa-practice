class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## solution 2: Snowball - Time O(N), Space O(1)
        i = 0  # Position for next non-zero element
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

        # ## solution 1: Time O(N), Space O(1)
        # n = len(nums)
        # def find_next_zero(i):
        #     while i<n:
        #         if nums[i]!=0:
        #             i+=1
        #         else:
        #             return i
        #     return i

        # i = find_next_zero(0)
        # j=i
        # while j<n:
        #     if nums[j]!=0:
        #         nums[i]=nums[j]
        #         nums[j]=0
        #         i = find_next_zero(i)
        #     j+=1
        # return nums
