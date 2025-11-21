class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        res = 0
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num in count:
            if num + 1 in count:
                if count[num] + count[num+1] > res:
                    res = count[num] + count[num+1]
        return res
