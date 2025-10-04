class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def helper(pairs):
            if (pairs == 1):
                return { "()" }

            bases = helper(pairs-1)
            res = set()
            for combo in bases:
                res.add("("+ combo + ")")
                res.add("()" + combo)
                res.add(combo + "()")
            print(res)
            return res
        
        results = helper(n)
        return [x for x in results]
        