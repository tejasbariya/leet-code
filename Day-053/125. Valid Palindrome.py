class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        r = ''
        for char in s:
            if  97 <= ord(char) <= 122 or 48<= ord(char) <= 57:
                r += char
        return r == r[::-1]        