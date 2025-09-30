class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        print("polygon", values)
        if (n < 3):
            return 0


        if (len(values) == 3):
            return values[0] * values[1] * values[2]

        base = values[0] * values[n-1]
        minScore = -1
        print("base",base)
        for k in range(1, n-1):
            triangleScore = base * values[k]
            print(triangleScore)
            score = self.minScoreTriangulation(values[k:]) + self.minScoreTriangulation(values[0:k+1]) + triangleScore

            print("score", score)
            if score < minScore or minScore == -1:
                minScore = score

        return minScore



        