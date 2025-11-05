class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexMap = {}

        i, j = 0, 0
        l = len(s)
        longest = 0
        while j < l:
            print(indexMap, i, j)
            c = s[j]
            if c in indexMap and indexMap[c] >= i:
                longest = max(longest, j-i)
                i = indexMap[c] + 1
            indexMap[c] = j
            j += 1
        longest = max(longest, j-i)
        return longest
        

        