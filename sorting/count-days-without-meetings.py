class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort(key=lambda x: x[0])
        meetings.append([days+1, days+1])
        # print(meetings)
        res = 0
        prev = 0
        for start, end in meetings:
            res += max(0, start-prev-1)
            # print(res)
            prev = end
        return res
