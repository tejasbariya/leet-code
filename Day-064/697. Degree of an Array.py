class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 
        maxFreq = 1
        data = {}
        for i in range(len(nums)):
            n = nums[i]
            if n not in data:
                data[n] = {}
                data[n]['f'] = i
                data[n]['l'] = i
                data[n]['c'] = 1
            else:
                data[n]['l'] = i
                data[n]['c'] += 1
                maxFreq = max(maxFreq, data[n]['c'])
        minLen = len(nums)
        for num in data:
            if data[num]['c'] == maxFreq:
                minLen = min(minLen, data[num]['l'] - data[num]['f'] + 1)
        return minLen
