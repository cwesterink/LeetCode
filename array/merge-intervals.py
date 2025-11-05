class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda interval: interval[0])

        print(intervals)
        intervalStart = intervals[0][0]
        intervalEnd =intervals[0][1]
        mergedIntervals = []
        for i in range(len(intervals)-1):
            int1 = intervals[i]
            int2 = intervals[i+1]
            if intervalEnd < int2[0]:
                mergedIntervals.append([intervalStart, intervalEnd])
                intervalStart = int2[0]
            intervalEnd = max(intervalEnd, int2[1])


        mergedIntervals.append([intervalStart,intervalEnd])

        return mergedIntervals
        