class Solution:
    def reverseVowels(self, s: str) -> str:
        # solution 2: cleaner approach: Time O(N), Space O(1)
        v = set("aeiouAEIOU")
        s = list(s)
        l, r = 0, len(s)-1
        while l < r:
            # Move left pointer to next vowel
            while l < r and s[l] not in v:
                l += 1
            
            # Move right pointer to next vowel
            while l < r and s[r] not in v:
                r -= 1
            
            # Swap vowels
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return "".join(s)
            
        # # solution 1: Time O(N), Space O(1)
        # v = set("aeiouAEIOU")
        # n = len(s)
        # s = list(s)
        
        # def next_v(i,inc):
        #     while -1<i<n:
        #         if s[i] in v:
        #             return i
        #         else:
        #             i=i+inc
        #     return n if inc else 0

        # l,r = next_v(0,1), next_v(n-1,-1)
        # while l<r:
        #     s[l], s[r] = s[r], s[l]
        #     l,r = next_v(l+1,1), next_v(r-1,-1)
        # return "".join(s)
