class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original = image[sr][sc]
        if original == color:
            return image
        image[sr][sc] = color
        memo = []
        n1 = len(image)
        n2 = len(image[0])
        def fill(i, j):
            # up
            if i > 0 and image[i-1][j] == original:
                image[i - 1][j] = color
                memo.append([False, i - 1, j])
            # left
            if j > 0 and image[i][j-1] == original:
                image[i][j - 1] = color
                memo.append([False, i, j - 1])
            # down
            if i + 1 < n1 and image[i+1][j] == original:
                image[i + 1][j] = color
                memo.append([False, i + 1, j])
            # right
            if j + 1 < n2 and image[i][j + 1] == original:
                image[i][j + 1] = color
                memo.append([False, i, j + 1])
        fill(sr, sc)
        for place in memo:
            if not place[0]:
                fill(place[1], place[2])
        return image