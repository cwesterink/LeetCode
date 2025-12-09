class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        prefixSum = []
        prev = 0
        low = 0
        hi =0
        for val in nums:
            prev += val
            if prev < low:
                low = prev
            if prev > hi:
                hi = prev
        return hi-low

        -4
        2

        
        

        