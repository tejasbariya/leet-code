class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        sol = []
        n = len(nums)
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break

            if  nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            
            r1 = n - 1
            while r1 > i + 2:
                if r1 < n-1 and nums[r1] == nums[r1+1]:
                    r1 -= 1
                    continue

                if nums[i] + nums[i+1] + nums[i+2] + nums[r1] > target:
                    r1 -= 1
                    continue

                if  nums[i] + nums[r1-1] + nums[r1-2] + nums[r1] < target:
                    break

                l, r = i + 1, r1 - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r] + nums[r1]
                    if s == target:
                        sol.append([nums[i], nums[l], nums[r], nums[r1]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r - 1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s > target:
                        r -= 1
                    else:
                        l += 1
                r1 -= 1      
        return sol