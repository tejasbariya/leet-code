class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType)
        candies_eaten = n // 2
        i = 0
        
        candyType.sort()
        for i in range(n):
            if i > 0 and candyType[i] == candyType[i-1]:
                continue
            if candies_eaten  == 0:
                break
            candies_eaten -= 1
            
        return n //2 - candies_eaten