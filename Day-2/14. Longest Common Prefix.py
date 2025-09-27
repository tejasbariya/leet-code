class Solution:
    def longestCommonPrefix(self, strs) -> str:

        if len (strs) == 0: return ""
        if len(strs) == 1:
            return strs
        minlen = len(strs[0])
        for i in range((len(strs))):
            if len(strs[i]) < minlen :
                minlen=len(strs[i])

        flag  = True
        lcp = ''
        for i in range(minlen):
            temp = strs[0][i]
            for word in strs:
                if temp == word[i]:
                    continue
                else :
                    flag = False
                    break
            if flag :
                lcp += temp
            else :
                return lcp

        return lcp
