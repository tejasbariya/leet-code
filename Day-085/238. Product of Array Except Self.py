class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        count = 0
        for num in nums:
            if num:
                mul *= num
            else:
                count += 1
        if count == 0:
            return [mul // num for num in nums]
        elif count == 1:
            return [0 if num else mul for num in nums]
        else:
            return [0] * len(nums)
