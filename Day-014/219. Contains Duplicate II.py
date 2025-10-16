class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return True
            visited.add(nums[i])
            if len(visited) > k:
                visited.remove(nums[i-k])
        return False