class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        record = {}
        strings = list((set(list1) & set(list2)))
        for string in strings:
            record[string] = list1.index(string) + list2.index(string)
        
        return [string for string, val in record.items() if val == min(record.values())]