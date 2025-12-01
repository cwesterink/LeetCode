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
        
        print(prefixMap)
        while len(prefixMap) > 0:
            s, count = prefixMap.popitem()
            
            a = s-k
            print(s, count, a)
            if a == 0:
                res += count
            elif a in prefixMap:
                countOther = prefixMap[a]
                res += count * countOther
            

        return res
        