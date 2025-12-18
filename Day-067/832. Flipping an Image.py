class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        new_img = []
        for row in image:
            new_img.append([1 - val for val in row[::-1]])
        return new_img
