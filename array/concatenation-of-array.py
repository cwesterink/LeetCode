class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = []
        for i in range(l*2):
            res.append(nums[i%l])
        return res
        