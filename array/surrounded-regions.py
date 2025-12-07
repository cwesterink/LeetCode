class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        edges = [
            (0, i) for i in range(cols)] + [
                (rows-1, i) for i in range(cols)] + [
                (i, 0) for i in range(rows)] + [
                (i, cols-1) for i in range(rows)]

        def replace(i, j, s, d):
            if i < 0 or j < 0 or j >= cols or i >= rows:
                return
            if board[i][j] == s:
                board[i][j] = d
                replace(i+1, j, s, d)
                replace(i-1, j, s, d)
                replace(i, j+1, s, d)
                replace(i, j-1, s, d)
                
        for i, j in edges:
            replace(i, j, 'O', 'T')
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i, j in edges:
            replace(i, j, 'T', 'O')