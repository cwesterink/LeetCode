class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        

        def helper(i):
            if i >= n-1:
                return True
            
            for j in range(i+1, i + nums[i]+ 1):
                if helper(j):
                    return True
            return False

        return helper(0)
        