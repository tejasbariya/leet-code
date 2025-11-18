class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        def isInRow(row, word,i):
            for char in word:
                if char not in row:
                    return 
            res.append(words[i])
        for i in range(len(words)):
            word = words[i].lower()
            if word[0] in "qwertyuiop":
                row = "qwertyuiop"
            elif word[0] in "asdfghjkl":
                row = "asdfghjkl"
            else:
                row = "zxcvbnm"
            isInRow(row, word, i)
        return res