class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for val in nums:
            if val % 3 != 0:
                res += 1
        return res
        