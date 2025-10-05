class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## solution 1
        if len(set(nums))!= len(nums):
            return True
        else:
            return False
