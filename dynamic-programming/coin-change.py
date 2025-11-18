class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = [None for i in range(amount+1)]
        memo[0] = 0
        def helper(i):
            if i < 0:
                return -1
            
            if memo[i] == None:
                # Try each coin
                valid_results = []
                for coin in coins:
                    result = helper(i - coin)
                    if result != -1:  # Only consider valid results
                        valid_results.append(result)
                if len(valid_results) == 0:
                    memo[i] =  -1
                    return -1
                memo[i] = 1 + min(valid_results)
            return memo[i]

        return helper(amount)
        