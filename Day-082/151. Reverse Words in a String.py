class Solution:
    def reverseWords(self, s: str) -> str:
        r = s.split(' ')
        for i in range(len(r)- 1, -1, -1):
            if r[i] == '':
                r.pop(i)
        return ' '.join(r[::-1])
