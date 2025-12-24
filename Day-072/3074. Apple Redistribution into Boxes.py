class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        capacity.sort(reverse=True)
        need = sum(apple)
        for i in range(len(capacity)):
            need -= capacity[i]
            if  0 >= need:
                break
        return i + 1
