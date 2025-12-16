class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = k = 0
        while i < len(bits):
            if bits[i] == 1:
                k = 1
                i += 1
            else:
                k = 0
            i += 1
        if k == 1:
            return False
        return bits[-1] == 0