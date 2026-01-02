class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            if nums.count(num) * 2 == n:
                return num
