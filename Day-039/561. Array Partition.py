class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        res = 0
        while i < len(nums):
            res += nums[i]
            i += 2
        return res