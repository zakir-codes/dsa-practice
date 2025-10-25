class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ## solution 1: Time O(N^2) Space O(N)
        res = [1]
        for _ in range(rowIndex):
            # update in reverse to avoid overwriting
            for i in range(len(res) - 1, 0, -1):
                print(i)
                res[i] += res[i - 1]
            res.append(1)
        return res
