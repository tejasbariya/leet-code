class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for n1 in range(len(nums) -1):
                if nums[n1] == nums[n1 +1]:
                    return True
        return False