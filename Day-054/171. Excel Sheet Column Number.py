class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        r = 0
        columnTitle = columnTitle[::-1]
        for i in range(len(columnTitle)):
            r += (26 ** i) * (ord(columnTitle[i]) - 64)
        return r