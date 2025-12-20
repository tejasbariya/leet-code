class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        need = [0] * 26
        for ch in licensePlate:
            if ch.isalpha():
                ch = ch.lower()
                need[ord(ch) - ord('a')] += 1
        
        ans = None
        for word in words:
            count = [0] * 26
            for ch in word:
                if ch.isalpha():
                    ch = ch.lower()
                    count[ord(ch) - ord('a')] += 1
            
            ok = True
            for i in range(26):
                if count[i] < need[i]:
                    ok = False
                    break
            
            if ok:
                if ans is None or len(word) < len(ans):
                    ans = word
        
        return ans
