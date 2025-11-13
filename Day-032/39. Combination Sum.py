class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, comb, total):
            if total == target:
                res.append(list(comb))
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb, total + candidates[i])
                comb.pop()

        backtrack(0, [], 0)
        return res
