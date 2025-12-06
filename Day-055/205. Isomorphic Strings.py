class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        maping = {}
        maping2 = {}
        for i in range(len(s)):
            char = s[i]
            if char not in maping:
                if  t[i] not in maping2:
                    maping[s[i]] = t[i]
                    maping2[t[i]] = char
                else:
                    return False
            elif maping[char] != t[i]:
                return False
        return True