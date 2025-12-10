class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MOD = 10 ** 9 + 7
        max_val = max(nums)  * 2  + 1
        fp = [0] * max_val
        fn = [0] * max_val

        for x in nums:
            fn[x] += 1
        ans = 0
        for x in nums:
            fn[x] -= 1
            t = x * 2
            ans = (ans + fn[t] * fp[t]) % MOD
            fp[x] += 1
        return ans