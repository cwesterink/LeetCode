class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.brute_force(board, word)


    def brute_force(self, board, word):
        rows, cols = len(board), len(board[0])
        lenWord = len(word)
        def search(i, j, c):
            if c == lenWord:
                return True
            
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False

            if board[i][j] == word[c]:
                board[i][j] = ''
                success = any([
                    search(i+1, j, c+1),
                    search(i-1, j, c+1),
                    search(i, j+1, c+1),
                    search(i, j-1, c+1)
                ])
                board[i][j] = word[c]
                return success

            return False

        for i in range(rows):
            for j in range(cols):
                if search(i, j, 0):
                    return True
        return False
                

        
            
        