class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = [None for i in range(len(nums))]

        # longes result given last max val is i
        def helper(i):
            if memo[i] != None:
                return memo[i]

            if i == len(nums):
                return 0

            best = 0
            for j in range(0, i):
                if nums[j] <  nums[i]:
                    best = max(best, helper(j))
            
            best += 1
            memo[i] = best
            return best

        return max([helper(i) for i in range(len(nums))])


            
