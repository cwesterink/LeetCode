class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        n = len(s)
        firstChange = -1
        start, end = 0, 0
        replacementsUsed = 0
        while end < n:
            if s[end] != s[start]:
                if firstChange == -1:
                    firstChange = end
                replacementsUsed += 1
                if replacementsUsed > k:
                    longest = max(longest, end-start)
                    replacementsUsed = 0
                    start = end = firstChange
                    firstChange = -1
            end += 1
        longest = max(longest, end-start+k-replacementsUsed)
        return longest
        
            

