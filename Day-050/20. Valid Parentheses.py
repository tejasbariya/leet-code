class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        x = []
        for char in s:
            if char in a:
                t = x.pop() if x else ''
                if a[char] != t:
                    return False
            else:
                x.append(char)
        
        return not len(x)