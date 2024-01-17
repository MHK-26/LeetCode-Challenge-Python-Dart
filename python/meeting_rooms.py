"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda intr: intr.start)  # Sort intervals by starting time

        for i in range(1, len(intervals)):
            m = intervals[i - 1]  # Previous interval
            n = intervals[i]     # Current interval
            if m.end > n.start:   # Check for overlap
                return False      # Conflict found, return False

        return True             # No conflicts found, return True
