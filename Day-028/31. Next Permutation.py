class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        flag = True
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                l = i
                flag = False
                break
        if flag:
            nums.sort()
            return
        r = l+1
        y = nums[l]
        for i in range(n-1, r, -1):
            if y < nums[i]:
                r = i
                break
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1