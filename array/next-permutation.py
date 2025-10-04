class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        l = len(nums)
        prev = -1
        for i in range(l-1, -1, -1):
            cur = nums[i]
            if (prev > cur):
                nums[i], nums[i+1] = prev, cur
                break
            prev = cur
        else:
            nums.sort()
        
        """
        Do not return anything, modify nums in-place instead.
        """
        