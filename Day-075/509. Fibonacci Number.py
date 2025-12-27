class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, a + b
        return b