class Solution:
    def maxPower(self, s: str) -> int:
        max_power = curr_power = 1
        prev_char = s[0]
        n = len(s)
        for i in range(1, n):
            if s[i] == prev_char:
                curr_power += 1
                max_power = max(max_power, curr_power)
            else:
                curr_power = 1
                prev_char = s[i]
        return max_power
