class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        l = len(triangle)

        def helper(row, col):
            if row > l-1:
                return 0

            path = min(helper(row+1, col), helper(row+1, col+1))
            return path + triangle[row][col]

        return helper(0, 0)

        