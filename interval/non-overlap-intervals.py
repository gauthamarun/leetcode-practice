class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        count = 0
        prev_end = intervals[0][1]
        for interval in intervals[1:]:
            if prev_end>interval[0]:
                prev_end = min(prev_end, interval[1])
                count+=1
            else:
                prev_end = interval[1]
        return count           