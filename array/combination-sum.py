class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def helper(arry, x, j):
            if x == 0:
                results.append(arry)
            if x <= 0:
                return

            for i in range(j, len(candidates)):
                val = candidates[i]
                helper(arry+[val], x-val, i)
            return
        
        helper([], target, 0)
        return results
            



        