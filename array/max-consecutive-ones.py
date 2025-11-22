class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        streak = 0
        nums.append(0)
        for val in nums:
            if val == 0:
                if streak > best:
                    best = streak
                streak = 0
            else:
                streak += 1
        return best
            
        