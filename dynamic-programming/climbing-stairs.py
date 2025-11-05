class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1): return 1
        memo = [-1 for i in range(n+1)]
        memo[1] = 1
        memo[2] = 2

        def helper(i):
            if memo[i] == -1:
                memo[i] = helper(i-1) + helper(i-2)
            return memo[i]
        
        return helper(n)
        