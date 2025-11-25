class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] == nums[i]:
                break
        for j in range(n):
            if j + 1 not in nums:
                break
        return [nums[i] , j + 1]