class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## solution: Time: O(N²) Space: O(N)
        if not s:
            return ""
        
        longest = ""
        
        def expand_from_center(left, right):
            """Expands outward from a center point (or two points)"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome found (s[left+1 : right])
            return s[left + 1 : right]

        for i in range(len(s)):
            # Odd length palindromes (center is a single character)
            p1 = expand_from_center(i, i)
            if len(p1) > len(longest):
                longest = p1
            
            # Even length palindromes (center is between two characters)
            p2 = expand_from_center(i, i + 1)
            if len(p2) > len(longest):
                longest = p2
                
        return longest
