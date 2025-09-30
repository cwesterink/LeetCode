class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        length = len(values)
        memoTable = [[-1 for _ in range(length)] for _ in range(length)]

        def helper(start, end):
            memoRes = memoTable[start][end-1]
            if (memoRes != -1): return memoRes

            n = end - start

            if (n < 3):
                memoTable[start][end-1] = 0
                return 0

            if (n == 3):
                memoTable[start][end-1] = values[start] * values[start+1] * values[start+2]
                return memoTable[start][end-1]

            base = values[start] * values[end-1]
            minScore = -1
            # print("base",base)
            for k in range(start+1, end-1):
                triangleScore = base * values[k]
                score = helper(k, end) + helper(start, k+1) + triangleScore

                # print("score", score)
                if score < minScore or minScore == -1:
                    minScore = score

            memoTable[start][end-1] = minScore
            return minScore


        return helper(0, length)




        