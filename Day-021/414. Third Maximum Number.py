class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        print(nums)
        if len(nums) > 2:
            return nums[len(nums) - 3]
        return max(nums)
        