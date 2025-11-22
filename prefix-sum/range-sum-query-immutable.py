class NumArray:

    def __init__(self, nums: List[int]):
        self.rollingSum = []
        s = 0
        for i in nums:
            s += i
            self.rollingSum.append(s)
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.rollingSum[right]
        return self.rollingSum[right] - self.rollingSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)