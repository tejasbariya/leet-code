class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = nums[0]
        count = 1
        max = count
        n = len(nums)
        for i in range(1, n):
            if curr < nums[i] :
                count += 1
                if count > max:
                        max = count
            else:
                count = 1
            curr = nums[i]
        if count > max:
                    max = count
        return max