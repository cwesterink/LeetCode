class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        res = []
        reach = 0
        start = 0
        for i, c in enumerate(s):
            reach = max(reach, last[c])

            if i == reach:
                res.append(reach-start+1)

                start = i + 1
    
        return res

        