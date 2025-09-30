class Solution:
    def searchInsert(self, nums, target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end - start) //2 
            if nums[mid] == target:
                return mid
            print(f"start:{start}, mid:{mid}, end:{end}, num:{nums[mid]}")
            if nums[mid] < target:
                end = mid - 1
            else:
                start = mid + 1

        return start
