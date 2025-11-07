class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (j+i) // 2

            midVal = nums[mid]
            if midVal == target:
                return mid
 
            if midVal > target:
                j = mid - 1
            else:
                i = mid + 1

        return -1
        