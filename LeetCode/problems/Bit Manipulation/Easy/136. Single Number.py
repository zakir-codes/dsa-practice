class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## solution 1: Time O(N); Space O(1)
        res = 0
        for n in nums:
            res ^= n
        return res
