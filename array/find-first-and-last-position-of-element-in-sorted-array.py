class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1

        start = -1
        while i <= j:
            mid = (i + j) // 2
            val = nums[mid]
            print(mid, val)
            if val == target and (mid == 0 or nums[mid-1] != target):
                # first match found
                start = mid
                break
            
            elif val >= target:
                j = mid -1
            else:
                i = mid + 1
        
        if start == -1:
            return [-1, -1]
        
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            val = nums[mid]

            if val == target and (mid == len(nums)-1 or nums[mid+1] != target):
                # first match found
                return [start, mid]
            
            elif val <= target:
                i = mid + 1
            else:
                j = mid - 1
    
        
