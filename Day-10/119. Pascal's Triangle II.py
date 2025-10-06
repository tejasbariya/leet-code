class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        for i in range(rowIndex+1):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i :
                    val = 1
                else:
                    val = prev[j-1] + prev[j]
                temp.append(val)
            prev = temp
        return temp