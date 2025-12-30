class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count = i = 0
        end = len(word)
        dp = []
        for i in range(len(sequence)):
            count = 0
            x = i
            while x <= len(sequence):
                if word == sequence[x : end + x]:
                    count += 1
                    x += end
                else:
                    dp.append(count)
                    break
        return max(dp)
