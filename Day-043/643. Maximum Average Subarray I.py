class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum1 = sum(nums[:k])
        sum2 = sum1
        for i in range(k, len(nums)):
            sum1 += nums[i] - nums[i-k]
            sum2 = max(sum1, sum2)
        return float(sum2) /k 