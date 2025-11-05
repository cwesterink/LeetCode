class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda interval: interval[0])

        intervalStart = intervals[0][0]
        mergedIntervals = []
        for i in range(len(intervals)-1):
            int1 = intervals[i]
            int2 = intervals[i+1]
            if int1[1] < int2[0]:
                mergedIntervals.append([intervalStart, int1[1]])
                intervalStart = int2[0]


        mergedIntervals.append([intervalStart, int2[1]])

        return mergedIntervals
        