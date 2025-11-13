class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in wordMap:
                wordMap[key] = [s]
            else:
                wordMap[key].append(s)
        return list(wordMap.values())
        