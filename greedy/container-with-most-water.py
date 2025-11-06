class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol = 0

        i, j = 0, len(height)-1

        while i < j:
            lWall = height[i]
            rWall = height[j]

            vol = min(lWall, rWall) * (j-i)
            maxVol = max(vol, maxVol)

            if rWall > lWall:
                i += 1
            else:
                j -= 1
        return maxVol
