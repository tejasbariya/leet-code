class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = j =0
        r = ''
        n1 = len(word1)
        n2 = len(word2)
        while i < n1 and j < n2:
            r += word1[i]
            r += word2[j]
            i += 1
            j += 1
        while i < n1:
            r += word1[i]
            i += 1
        while j < n2:
            r += word2[j]
            j += 1
        return r