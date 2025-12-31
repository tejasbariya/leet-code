class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        r = []
        total_candy = max(candies)
        for no_candy in candies:
            r.append(total_candy <= no_candy + extraCandies)
        return r