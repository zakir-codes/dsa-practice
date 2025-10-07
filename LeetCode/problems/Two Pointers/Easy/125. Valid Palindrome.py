class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## solution 1
        # preprocess the string
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)

        # match first and second half
        n_2 = len(s)//2
        s2_idx = n_2 + (len(s) % 2)
        
        if s[:n_2]==s[s2_idx:][::-1]:
            return True
        return False
