class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = [[0 for _ in range(m)] for _ in range(n)]
        memo[-1][-1] = 1

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                val = 0
                if i + 1 < n:
                    val += memo[i+1][j]
                if j + 1 < m:
                    val += memo[i][j+1]
                if val == 0: continue

                memo[i][j] = val
        
        return memo[0][0]
        