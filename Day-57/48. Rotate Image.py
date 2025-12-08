class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n1 = len(matrix)
        n2 = len(matrix[0])
        for i in range(n1):
            l, r =0, n2-1
            while l< r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
            print(matrix)
        r1, c1 = 0, 0
        r2, c2 = n1 - 1 , n2- 1
        while r1< n1 and c2 >= 0:
            c1 = 0
            r2 = n1-1
            while c1 < n2 - r1 and r2 >= 0 + r1:
                matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
                c1 += 1
                r2 -= 1
            r1 +=1
            c2 -=1