class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        res = []
        candidates.sort()
        def backtrack(start, combi, total):
            if total == target:
                res.append(list(combi))
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i  > start and candidates[i] == candidates[i -1]:
                    continue
                combi.append(candidates[i])
                backtrack(i+1, combi, total + candidates[i])
                combi.pop()
        backtrack(0, [], 0)
        return res