class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        satisfied_child = i = j = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                satisfied_child += 1
                i += 1
                j += 1
            elif g[i] > s[j]:
                j += 1
        return satisfied_child
        