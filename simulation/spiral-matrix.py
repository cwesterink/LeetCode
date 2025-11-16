class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        n = len(matrix)
        m = len(matrix[0])

        totalCells = n * m

        i, j = 0, 0
        leftWall, topWall = 1, 1
        rightWall, bottomWall = m-1, n-1

        while True:
            print(i, j)
            if j >= rightWall:
                break
            while j < rightWall:
                res.append(matrix[i][j])
                j += 1
                
            topWall += 1
            if i >= bottomWall:
                break
            while i < bottomWall:
                res.append(matrix[i][j])
                i += 1
            rightWall -= 1
            if j < leftWall:
                break
            while j >= leftWall:
                res.append(matrix[i][j])
                j -= 1

            bottomWall -= 1
            if i < topWall:
                break
            while i >= topWall:
                res.append(matrix[i][j])
                i -= 1
            leftWall += 1
        res.append(matrix[i][j])

        return res


        

        