class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c :
            return mat
        res = []
        x = y = 0
        for i in range(m):
            for j in range(n):
                curr = mat[i][j]
                if x < r:
                    if y == 0:
                        row = []
                    row.append(curr)
                    y += 1
                    if y == c:
                        y = 0
                        x += 1
                        res.append(row)
        return res