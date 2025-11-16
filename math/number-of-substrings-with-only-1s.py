class Solution:
    def numSub(self, s: str) -> int:

        cap = 10**9 + 7
        streak = 0
        streakFreq = {}
        for i, x in enumerate(s):
            if streak > 0 and x == '0':
                if streak not in streakFreq:
                    streakFreq[streak] = 0
                streakFreq[streak] += 1
                streak = 0
            
            if x == '1':
                streak += 1
        
        print(streak)
        if streak > 0:
            if streak not in streakFreq:
                streakFreq[streak] = 0
            streakFreq[streak] += 1

        print(streakFreq)
        res = 0
        for streak, count in streakFreq.items():
            res += count * (streak * (streak + 1)//2)
        return res % cap

        