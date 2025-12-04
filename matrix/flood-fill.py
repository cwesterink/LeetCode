class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        n,m  = len(image), len(image[0])
        def helper(i, j, c):
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if image[i][j] != c:
                return
            image[i][j] = color
            helper(i+1, j, c)
            helper(i-1, j, c)
            helper(i, j+1, c)
            helper(i, j-1, c)
        if color != image[sr][sc]:
            helper(sr, sc, image[sr][sc])

        return image

        