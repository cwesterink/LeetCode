class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        e = (n * (n+1))//2
        seen = set()
        dup = -1

        for num in nums:
            if num in seen:
                dup = num
                break
            seen.add(num)
        s = sum(nums)
        return [dup, e-(s-dup)]
        