class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ## Solution 2; Time O(N), Space O(1)
        n, m = len(sequence), len(word)
        max_k = 0
        i = 0

        while i <=n:
            k = 0
            while sequence[i:i + m*(k+1)] == word*(k+1):
                k += 1
            max_k = max(max_k, k)
            i += 1 # m*k if k>0 else 1
        return max_k
        
        # ## Solution 1; Time O(N^2), Space O(1)
        # max_k = 0
        # for i in range(len(sequence)):
        #     k = 0
        #     while sequence[i:i + len(word)*(k+1)] == word*(k+1):
        #         k += 1
        #     max_k = max(max_k, k)
        # return max_k
