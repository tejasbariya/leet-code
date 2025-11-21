class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        min1 = ops[0][0]
        min2 = ops[0][1]
        for row in ops:
            if row[0] < min1:
                min1 = row[0]
            if row[1] < min2 :
                min2 = row[1]

        return min1 * min2