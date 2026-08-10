class Solution(object):
    def merge(self, intervals):
        result = []
        intervals.sort(key=lambda intervals:intervals[0])

        if len(intervals)==1:
            return intervals

        for interval in intervals:
            if result and interval[0]<=result[-1][1]:
                result[-1][1]= max(result[-1][1], interval[1]) 
            else:
                result.append(interval)    

        return result