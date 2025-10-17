class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        openP = { '(', '[', '{'}
        closeP = {')', ']', '}'}
        for c in s:
            if c in openP:
                queue.append(c)
            else:
                o = queue.pop()
                if (o == "(" and c != ")"):
                    return False
                if (o == "{" and c != "}"):
                    return False
                if (o == "[" and c != "]"):
                    return False
        return len(queue) == 0

        