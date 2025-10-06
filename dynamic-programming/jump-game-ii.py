class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        memoTable = [-1 for i in range(n)]


        def helper(i):
            if i == n-1:
                return 0
            if i > n-1:
                return -1

            maxDist = nums[i]
            if (maxDist == 0):
                return -1

            bestJump = -1
            for j in range(i+1, i+maxDist+1):
                d = helper(j)
                print(j, ": jumpt to",d)
                if d == -1:
                    continue
                
                if d < bestJump or bestJump == -1:
                    bestJump = d

            return 1 + bestJump
        
        return helper(0)


        