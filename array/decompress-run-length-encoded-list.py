class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n//2):
            freq, val = nums[2*i:2*i+2]
            res += [val] * freq
        return res

        