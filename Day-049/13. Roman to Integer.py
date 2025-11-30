class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rt = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            "M":1000,
        }
        r = rt[s[0]]
        for i in range(1, len(s)):
            if rt[s[i-1]] >= rt[s[i]]:
                r += rt[s[i]]
            else:
                r += rt[s[i]] - rt[ s[i-1]] * 2
        
        return r
