class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        r = []
        for num in set(arr):
            c = arr.count(num)
            if c in r:
                return False
            r.append(c)
        return True
