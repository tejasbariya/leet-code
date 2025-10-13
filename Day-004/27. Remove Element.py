class Solution:
    def removeElement(self, nums, val: int) -> int:
        temp = []
        for num in nums:
            if num  != val:
                temp.append(num)

        i = 0
        for t in temp:
            nums[i] = t
            i += 1
        return i
    