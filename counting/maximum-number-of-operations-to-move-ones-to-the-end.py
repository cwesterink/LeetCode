class Solution:
    def maxOperations(self, s: str) -> int:
        i = 0
        l = len(s)
        numOnes = 0
        operations = 0
        while i < l:
            if s[i] == '1':
                numOnes += 1
                i += 1
            else:
                while i < l and s[i] == '0':
                    i += 1
                operations += numOnes
        return operations


        