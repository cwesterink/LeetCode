class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if (l == 0):
            return []
        if (l == 1):
            return [[], [nums[0]]]
        
        n = nums.pop()
        res = self.subsets(nums)
        return res + [[n]+s for s in res]

        