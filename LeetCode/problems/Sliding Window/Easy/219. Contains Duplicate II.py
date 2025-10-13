class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## solution 1
        win = set()
        for i, num in enumerate(nums):

            if num in win:
                return True
            win.add(num)

            if i>=k:
                win.remove(nums[i-k])

        return False
