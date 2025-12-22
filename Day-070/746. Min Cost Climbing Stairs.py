class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0] * n
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(n-3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return dp[0] if dp[0] < dp[1] else dp[1]