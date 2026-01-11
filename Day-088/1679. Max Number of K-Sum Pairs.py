class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        i, j = 0, n - 1
        count = 0
        while i < j:
            x = nums[i] + nums[j]
            if x == k:
                count += 1
                i += 1
                j -= 1
            elif x < k:
                i += 1
            else:
                j -= 1
        return count