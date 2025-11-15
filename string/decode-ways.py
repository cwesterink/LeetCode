class Solution:
    def numDecodings(self, s: str) -> int:

        memo = [-1 for i in range(len(s)+1)]

        memo[0] = 1
        memo[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, len(s)+1):
            j = i-1
            ways = 0
            uno = int(s[j])
            duo = int(s[j-1:j+1])

            if uno != 0:
                ways += memo[i-1]
            if duo > 9 and duo < 27:
                ways += memo[i-2]
            memo[i] = ways

        return memo[len(s)]


        