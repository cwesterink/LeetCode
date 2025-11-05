class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = dict()

        for i in range(len(nums)):
            val = nums[i]
            if (target - val in indexMap):
                return [indexMap[target-val], i]
            indexMap[val] = i
        
        