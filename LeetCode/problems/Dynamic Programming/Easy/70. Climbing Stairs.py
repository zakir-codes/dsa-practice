class Solution:
    def climbStairs(self, n: int) -> int:
        # solution 1: Time O(N); Space O(1)
        # edge case 1, 2
        if n<3:
            return n
        
        a,b = 1,2
        for i in range(3,n+1):
            b,a = a+b, b
        return b
