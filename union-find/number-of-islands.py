class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n, m  = len(grid), len(grid[0])

        def exploreIsland(i, j):
            if i >= n or j >= m or i < 0 or j < 0:
                return

            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            exploreIsland(i+1, j)
            exploreIsland(i-1, j)
            exploreIsland(i, j+1)
            exploreIsland(i, j-1)

        numIslands = 0
        for i in range(n):
            for j in range(m):
                cell = grid[i][j]

                if cell == "1":
                    numIslands += 1
                    exploreIsland(i, j)
        return numIslands



        