class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = len(nums)
        i, j = 0, len(nums) - 1
        m = 0
        while i < j:

            m = (i+j) // 2
            print(i, m, j)
            if m +1 < l and nums[m] > nums[m+1]:
                print("found break")
                break
            if nums[m] < nums[i]:
                j = m -1
            else:
                i = m +1

        if target >= nums[l-1]:
            # start array
            i, j = 0, m
        else:
            # end array
            i, j = m + 1, l-1

    
        while i <= j:
            m = (i+j) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                j = m - 1
            else:
                i = m + 1
        return -1
        