class Solution:
    def isPalindrome(self, x: int) -> bool:
        ## solution 1
        if x<0:
            return False

        x = str(x)
        n_2 = len(x)//2
        for i in range(n_2):
            if  x[i]!=x[-1-i]:
                return False
        return True
