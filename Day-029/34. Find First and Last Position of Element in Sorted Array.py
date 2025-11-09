class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        start = 0
        end = n- 1
        mid = 0
        flag = True
        while start <= end:
            mid = start + (end - start)// 2
            if nums[mid] == target:
                start = end = mid
                while start > 0 and nums[start] == nums[start-1]:
                    start -= 1
                while end < n-1 and nums[end] == nums[end+1]:
                    end += 1
                return [start, end]
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return [-1, -1]
        
        