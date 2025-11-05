class Solution:
    def rob(self, nums: List[int]) -> int:

        numHouses = len(nums)
        memo = [-1 for i in range(numHouses)]
        memo[-1] = nums[-1]

        def helper(i):
            if i >= numHouses:
                return 0
            if memo[i] == -1:
                memo[i] = max(nums[i] + helper(i+2), helper(i+1))
            
            return memo[i]

        return helper(0)
        