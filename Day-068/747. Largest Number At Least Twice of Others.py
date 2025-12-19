class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = max(nums)
        index = nums.index(m1)
        nums.remove(m1)
        if max(nums) * 2 <= m1:
            return index
        return -1