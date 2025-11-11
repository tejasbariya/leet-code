class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = 9
        columns = 9
        for r in range(rows):
            nums = []
            for c in range(columns):
                box = board[r][c]
                if box != ".":
                    if box not in nums:
                        nums.append(box)
                    else:
                        return False
        for c in range(columns):
            nums = []
            for r in range(rows):
                box = board[r][c]
                if box != ".":
                    if box not in nums:
                        nums.append(box)
                    else:
                        return False
        
        for x in range(0,rows,3):
            for y in range(0, columns, 3):
                nums = []
                for r in range(x, x+3):
                    for c in range(y,y+3):
                        box = board[r][c]
                        if box != ".":
                            if box not in nums:
                                nums.append(box)
                            else:
                                return False
        return True
        

        