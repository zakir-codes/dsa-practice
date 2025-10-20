class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ## solution 2:Time Complexity: O(N) and Space O(N) or O(1) [If no overflow occurs]
        c = 1
        for i in range(len(digits)-1,-1,-1):
            s = digits[i]+c
            if s<10:
               digits[i]=s
               c = 0
               break
            digits[i] = 0
        return [1]+digits if c==1 else digits
        
        ## solution - time O(N) space O(N)
        # s = "".join([str(d) for d in digits])
        # s = int(s)+1
        # return [int(d) for d in str(s)]
