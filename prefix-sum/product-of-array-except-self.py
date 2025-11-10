class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [0 for i in range(len(nums))]
        suffixProduct = [0 for i in range(len(nums))]

        p = 1
        for i in range(len(nums)):
            p = p * nums[i]
            prefixProduct[i] = p
        
        p = 1
        for i in range(len(nums)-1, -1, -1):
            p = p * nums[i]
            suffixProduct[i] = p

        res = []
        p = 1
        for i in range(len(nums)):
            p = 1
            if i > 0:
                p *= prefixProduct[i-1]
            if i < len(nums) -1:
                p *= suffixProduct[i+1]

            res.append(p)
        return res
