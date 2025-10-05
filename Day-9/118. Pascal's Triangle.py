from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r =[]
        for x in range(1,numRows+1):
            temp = []
            for i in range(x):
                if x - 1 == i or i == 0 :
                    val = 1
                else:
                    val = prev[i-1] + prev[i]
                temp.append(val)
            prev = temp
            r.append(temp)  
        return r