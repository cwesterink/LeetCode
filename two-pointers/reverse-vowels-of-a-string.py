class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        def isVowel(c):
            return c.lower() in { 'a', 'i', 'e', 'o', 'u'}

        for c in s:
            if isVowel(c):
                vowels.append(c)
        res = ""
        for i in range(len(s)):
            c = s[i]
            if isVowel(c):
                res += vowels.pop()
            else:
                res += c
        return res