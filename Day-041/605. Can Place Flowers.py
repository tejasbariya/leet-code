class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        length = len(flowerbed)
        if n == 0:
            return True
        
        while i < length:
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i-1] == 0) and
                (i == length-1 or flowerbed[i+1] == 0)):
                
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
                i += 2
            else:
                i += 1
            
        return True if n == 0 else False