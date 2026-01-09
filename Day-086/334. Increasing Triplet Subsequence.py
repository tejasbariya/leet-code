class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        if nums[0] < nums[1] < nums[2] or nums[-3] < nums[-2] < nums[-1]:
            return True
        x = y = float('inf')
        for num in nums:
            if num <= x:
                x = num
            elif num <= y:
                y = num
            else:
                return True
        return False
