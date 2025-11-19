class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        ranks = sorted(enumerate(score), key= lambda x: -x)
        ans = [''] * n
        for r, (index, val) in enumerate(ranks):
            if r == 0:
                ans[index] = ("Gold Medal")
            elif r == 1:
                ans[index] =("Silver Medal")
            elif r == 2:
                ans[index] =("Bronze Medal")
            else:
                ans[index] = (str(r+1))
        return ans