class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        curEnd = 0
        curFarthest = 0
        
        for i in range(n - 1):
            curFarthest = max(curFarthest, i + nums[i])
            
            if i == curEnd:
                jumps += 1
                curEnd = curFarthest

                if curEnd >= n - 1:
                    break
        
        return jumps
