class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        palindromes = [(i,i) for i in range(n)]
        for i in range(n-1):
            if s[i] == s[i+1]:
                palindromes.append((i, i+1))

        longest = -1
        palindrome = ""
        while palindromes:
            i, j = palindromes.pop()
            if i-1 >= 0 and j+1 < n and s[i-1] == s[j+1]:
                palindromes.append((i-1, j+1))
            elif j-i > longest:
                    longest = j-i
                    palindrome = s[i:j+1]

        return palindrome

                

        