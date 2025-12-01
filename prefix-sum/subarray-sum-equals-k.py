class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)

        
        p = 0
        prefixMap = {}
        for val in nums:
            p += val
            if p not in prefixMap:
                prefixMap[p] = 0
            prefixMap[p] += 1
        
        while len(prefixMap) > 0:
            s, count = prefixMap.popitem()
            if s == k:
                res += count
            if (k - s) in prefixMap:
                countOther = prefixMap.pop(k-s)
                res += count * countOther

        return res
        