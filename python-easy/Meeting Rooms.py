# Given an array of meeting time interval objects consisting of start and end times
# [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        # sort the array based on start time
        i2 = sorted(intervals, key=lambda Interval: Interval.start)
        print(i2[0].start, i2[0].end)
        for i in range(1, len(intervals)):
            if i2[i].start>=i2[i-1].end:
                continue
            else:
                return False
        return True
    
