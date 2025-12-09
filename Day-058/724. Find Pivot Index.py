class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tsum = sum(nums)
        lsum = 0
        rsum = 0
        for i in range(len(nums)):
            rsum =  tsum - lsum - nums[i]
            if lsum == rsum:
                return i
            lsum += nums[i]
        return -1