class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## solution 2: Boyer-Moore Voting Algorithm
        ## Time O(N), Space O(1)
        candidate = None
        count = 0
        
        for num in nums:
            # Think about: when to change candidate, when to increment/decrement count
            if count==0:
                candidate = num
                count+=1
            elif candidate==num:
                count+=1
            else:
                count-=1

        return candidate
        # ## solution 1: Time O(N) Space O(N)
        # count = {}
        # n_2 = len(nums)/2
        # for n in nums:
        #     count[n] = count.get(n,0)+1
        # for key, val in count.items():
        #     if val>n_2:
        #         return key
