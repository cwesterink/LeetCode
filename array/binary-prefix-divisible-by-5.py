class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        prev = 0
        res = []
        for i in nums:
            prev = prev * 2 + i
            res.append(prev % 5 == 0)
        return res
        