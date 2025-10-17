class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                  return True
            visited.add(nums[i])
        return False