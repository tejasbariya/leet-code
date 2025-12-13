class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        map1 = {}
        map2 = {}
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if pattern[i] not in map1:
                if s[i] not in map2:
                    map1[pattern[i]] = s[i]
                    map2[s[i]] = pattern[i]
                else:
                    return False
            elif map1[pattern[i]] != s[i] or map2[s[i]] != pattern[i]:
                return False
        return True