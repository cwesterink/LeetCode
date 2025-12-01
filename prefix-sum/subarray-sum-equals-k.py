class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)

        
        p = 0
        prefixSums = []
        for val in nums:
            p += val
            prefixSums.append(p)

        def sumRange(i, j):
            if i == 0:
                return prefixSums[j-1]

            return prefixSums[j-1] - prefixSums[i-1]
        for i in range(n):
            for j in range(i+1, n+1):
                if sumRange(i,j) == k:
                    res += 1
        return res
        