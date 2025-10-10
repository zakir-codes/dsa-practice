class Solution:
    def isHappy(self, n: int) -> bool:
        ## solution 2 - Floyd's Cycle Detection
        def get_next(num):
            return sum([int(digit)**2 for digit in str(num)])
        
        slow = n
        fast = get_next(n)
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1


        ## solution 1
        # tried = set()
        # while True:
        #     if n in tried:
        #         return False
        #     elif n==1:
        #         return True
        #     tried.add(n)
        #     n = sum([int(i)**2 for i in list(str(n))])
