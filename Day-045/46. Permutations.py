class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def per(l, left, right):
            if left  == right:
                res.append(list(l))
            else:
                for i in range( left,  right):
                    l[left], l[i] = l[i], l[left]
                    per(l, left + 1, right)
                    l[left], l[i] = l[i], l[left]
        per(nums, 0, len(nums))
        return res