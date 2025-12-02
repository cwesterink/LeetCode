class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        memo = [False for i in range(n+1)]
        memo[0] = True

        for i in range(n+1):
            if memo[i]:

                for word in wordDict:
                    if len(word) + i < n+1 and word == s[i:i+len(word)]:
                        memo[i+len(word)] = True
        return memo[-1]
        
        