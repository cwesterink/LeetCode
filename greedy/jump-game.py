class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)

        nums[-1] = 1
        dist = 1

        i = n-2
        while i >= 0:
            if dist > nums[i]:
                dist += 1
            else:
                dist = 1
            i -= 1
        return dist == 1

        