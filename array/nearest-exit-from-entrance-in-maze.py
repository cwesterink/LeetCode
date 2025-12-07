from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # BFS Problem
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        numRows = len(maze)
        numCols = len(maze[0])
        def isExit(i, j):
            return i == 0 or j == 0 or i == numRows -1 or j == numCols -1

        def inBounds(i, j):
            return (
                i < numRows and
                i >= 0 and 
                j < numCols and 
                j >= 0
            )
        def getAdjacentCells(i,j):
            res = []
            for r, c in directions:
                row = i + r
                col = j + c
                if inBounds(row, col) and maze[row][col] == ".":
                    res.append((row, col))
            return res

        queue = deque([entrance])
        dist = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                print(i,j)
                if isExit(i,j) and dist > 0:
                    return dist
                maze[i][j] = '+'
                dist += 1
                queue.extend(getAdjacentCells(i, j))
                
        return -1



        
        