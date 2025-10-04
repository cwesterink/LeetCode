class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if (len(nums) == 1):
            return [[nums[0]]]
        out = []
        for i in range(len(nums)):
            val = nums[i]
            subNums = nums[0:i] + nums[i+1:]
            res = self.permute(subNums)
            for p in res:
                out.append([val]+p)
        
        return out
        