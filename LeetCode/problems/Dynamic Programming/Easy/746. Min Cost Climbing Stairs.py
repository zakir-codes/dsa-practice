class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a,b = cost[0], cost[1]
        for c in cost[2:]:
            a,b = b, c+ min(a,b)
        return min(a,b)
