class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)

        
        s = 0
        prefixMap = {}
        prefixMap[0] = 1
        for val in nums:
            s += val
            l = s-k
            if l in prefixMap:
                countOther = prefixMap[l]
                res += countOther

            if s not in prefixMap:
                prefixMap[s] = 0
            prefixMap[s] += 1
        

        return res
        