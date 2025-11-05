class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lenght = len(nums)
        sol = float("inf")
        nums.sort()
        for i in range(lenght - 2):
            if 0 < i and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = lenght -1            
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if abs( sum3 - target ) < abs(sol - target):
                    sol = sum3
                if sum3 > target:
                    r -=1
                elif sum3 < target:
                    l += 1
                else :
                    return target
        return sol