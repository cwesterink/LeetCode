class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        res = 0
        n, m = len(grid), len(grid[0])


        def rot(i,j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if grid[i][j] == 1:
                grid[i][j] = 2
                return True
            return False

        rottenQueue = []
        directions = [(1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rottenQueue.append([i,j])

        mins = 0
        while len(rottenQueue) > 0:
            frontier = []
            mins += 1
            for i,j in rottenQueue:
                grid[i][j] = 0
                if rot(i+1, j):
                    frontier.append([i+1, j])
                if rot(i-1, j):
                    frontier.append([i-1, j])
                if rot(i, j+1):
                    frontier.append([i, j+1])
                if rot(i, j-1):
                    frontier.append([i, j-1])
            rottenQueue = frontier

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return mins -1
            

        