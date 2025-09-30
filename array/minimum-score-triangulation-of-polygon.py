class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        length = len(values)

        def helper(start, end):
            n = end - start

            if (n < 3):
                return 0

            if (n == 3):
                return values[start] * values[start+1] * values[start+2]

            base = values[start] * values[end-1]
            minScore = -1
            # print("base",base)
            for k in range(start+1, end-1):
                triangleScore = base * values[k]
                score = helper(k, end) + helper(start, k+1) + triangleScore

                # print("score", score)
                if score < minScore or minScore == -1:
                    minScore = score

            return minScore


        return helper(0, length)




        