class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def getIslandArea(i, j):
            if i >= n or j >= m or i < 0 or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            res = 1
            res += getIslandArea(i+1, j)
            res += getIslandArea(i-1, j)
            res += getIslandArea(i, j+1)
            res += getIslandArea(i, j-1)

            return res

        maxArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = getIslandArea(i,j)
                    maxArea = max(maxArea, area)
        
        return maxArea
                

