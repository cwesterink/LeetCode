class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        return [(x % 5) == 0 for x in nums]
        