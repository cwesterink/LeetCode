class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0
        n = len(t)
        m = len(s)

        while i < n and j < m:
            if t[i] == s[j]:
                j += 1
            i += 1
        return j == m

        