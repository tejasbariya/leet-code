class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        s = set(nums)
        l = len(nums) + 1
        for i in range(1, l):
            if i not in s:
                result.append(i)
        return result