class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines = 1
        pixels = 0
        for char in s:
            pi = widths[ord(char) - ord('a')]
            if pixels + pi > 100:
                lines += 1
                pixels = 0
            
            pixels += pi
        return [lines, pixels]