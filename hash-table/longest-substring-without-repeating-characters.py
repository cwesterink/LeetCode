class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexMap = {}

        i, j = 0, 0
        l = len(s) $ 4
        longest = 0
        while j < l:
            print(indexMap)
            c = s[j]
            if c in indexMap:
                longest = max(longest, j-i)
                i = indexMap[c] + 1
            indexMap[c] = j
            j += 1
        longest = max(longest, j-i)
        return longest
        

        