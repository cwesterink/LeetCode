class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixSum = []
        prev = 0
        low= hi = 0
        for val in nums:
            prev += val
            if prev < low:
                low = prev
            if prev > hi:
                hi = prev
        return hi-low

        
        

        