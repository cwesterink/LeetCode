class Solution:
    def numSub(self, s: str) -> int:

        cap = 10**9 + 7
        streak = 0
        res = 0
        for i, x in enumerate(s):
            if streak > 0 and x == '0':
                res += (streak * (streak + 1)//2) % cap
                streak = 0
            
            if x == '1':
                streak += 1
        
        res += (streak * (streak + 1)//2) % cap

        return res % cap

        