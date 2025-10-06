class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        memoTable = [-1 for i in range(n)]


        def helper(i):
            if i == n-1:
                memoTable[i] = 0
                return 0
            if i > n-1:
                return -1

            if memoTable[i] != -1:
                return memoTable[i]

            maxDist = nums[i]
            if (maxDist == 0):
                memoTable[i] = -1
                return -1

            bestJump = -1
            for j in range(i+1, i+maxDist+1):
                d = helper(j)
                if d == -1:
                    continue
                
                if d < bestJump or bestJump == -1:
                    bestJump = d

            if (bestJump == -1):
                memoTable[i] = -1
                return -1

            memoTable[i] = 1 + bestJump
            return 1 + bestJump
        
        return helper(0)


        