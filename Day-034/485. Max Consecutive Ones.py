class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        i = 0
        for n in nums:
            if n == 1:
                i += 1
            else:
                if x < i:
                    x = i
                i = 0
            if x < i:
                x = i
        return x