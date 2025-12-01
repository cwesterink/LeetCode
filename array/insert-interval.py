class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        res = []
        activeMerge = False

        for l, r in intervals:
            print(l, r, activeMerge)
            if activeMerge:
                if newInterval[1] < l:
                    res.append(newInterval)
                    activeMerge = False
                    res.append([l,r])
                elif newInterval[1] < r:
                    newInterval[1] = r
            else:
                if newInterval[0] <= r:
                    if newInterval[1] <= r:
                        res.append([l, r])
                    else:
                        newInterval[0] = l
                        activeMerge = True
                else:
                    res.append([l, r])

        if activeMerge:
            res.append(newInterval)
        return res



        