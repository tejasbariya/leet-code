class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts = [0, ]
        for alt in gain:
            alts.append(alts[-1] + alt)
        return max(alts)
