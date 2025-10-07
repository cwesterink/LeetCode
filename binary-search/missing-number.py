class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        mx = max(nums)
        while mx > 0:
            s -= mx
            mx -= 1
        
        if (s == 0):
            return max(nums)+1
        return -s
        