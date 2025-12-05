class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        columnNumber -= 1
        a = columnNumber % 26 
        b = columnNumber // 26
        if b > 0:
            return self.convertToTitle(b) + chr(65 + a)
        return chr(65 + a)