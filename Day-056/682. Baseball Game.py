class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        r = []
        for item in operations:
            if item == 'C':
                r.pop()
            elif item == 'D':
                r.append(r[-1] * 2)
            elif item == '+':
                r.append(r[-1] + r[-2])
            else:
                r.append(int(item))
        return sum(r)