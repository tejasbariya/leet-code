class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i = j = 0
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                land = grid[i][j]
                if not grid[i][j] :
                    continue
                if i == 0: up = 0
                else:up = grid[i-1][j]

                if i == len(grid)-1:down = 0
                else:down = grid[i+1][j] 

                if j == 0:left = 0
                else:left = grid[i][j-1]

                if j == len(grid[i])-1:right = 0
                else:right = grid[i][j+1]
                
                if not up   : peri += 1
                if not down : peri += 1
                if not left : peri += 1
                if not right: peri += 1
                print(f"land: {land} i:{i}, j:{j}, peri:{peri}")
        return peri

grid =[
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
]
s = Solution().islandPerimeter(grid)
print(s)