class Solution:
    def removeDuplicates(self, nums) -> int:
        x = 0
        arr = []
        for num in nums:
            if num not in arr:
                arr.append(num)
                x += 1

        for i in range(len(arr)):
            nums[i] =arr[i]

        print(nums)
        return x
