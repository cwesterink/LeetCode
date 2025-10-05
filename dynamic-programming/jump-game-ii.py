class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)

        def helper(i):
            if i == n-1:
                return 0
            
            maxDist = nums[i]
            if (maxDist == 0):
                return 10**4+1
            bestJump = min([helper(j) for j in range(i+1, i+maxDist+1)])

            return 1 + bestJump
        
        return helper(0)


        