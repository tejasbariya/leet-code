class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 1:
            return duration
        poisonedTime = 0
        for i in range(len(timeSeries)-1):
            diff = timeSeries[i+1] - timeSeries[i]
            if diff < duration:
                poisonedTime += diff
            else:
                poisonedTime += duration
        poisonedTime += duration
        return poisonedTime

        