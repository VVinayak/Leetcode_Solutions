#52 / 52 test cases passed.

#Runtime: 201 ms

#  We are given a list schedule of employees, which represents the working time for each employee.

# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order. 

#  (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)

# Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length. 

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from itertools import *

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        schedule = list(sorted(chain(*schedule), key=lambda interval: interval.start))
        busy_time_stack = [schedule[0]]
        free_time_stack = []
        for current_interval in schedule[1:]:
            top_interval = busy_time_stack[-1]
            if top_interval.end < current_interval.start:
                free_time_stack.append(Interval(top_interval.end,current_interval.start))
                busy_time_stack.append(current_interval)
            else:
                if current_interval.end < top_interval.end:
                    busy_time_stack.append(top_interval)
                else:
                    busy_time_stack.append(current_interval)
                    
        return free_time_stack
