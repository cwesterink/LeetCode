class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        deltaPos = { 0: -1}

        n = len(nums)
        delta = 0

        res = 0
        for i in range(n):
            val = nums[i]
            delta += 1 if val == 1 else -1
            if delta in deltaPos:
                res = max(res, i - deltaPos[delta])
            else:
                deltaPos[delta] = i
        return res
