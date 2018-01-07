#113 / 113 test cases passed.

#Runtime: 72 ms

#  An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.

# Find the minimum size of a set S such that for every integer interval A in intervals, the intersection of S with A has size at least 2. 

#--------------------------------------------------------------------------------------------------------------------------------------------
# First sort the intervals, with their starting points from low to high
# Then use a stack to eliminate the intervals which fully overlap another interval.
# For example, if we have [2,9] and [1,10], we can get rid of [1,10]. Because as long as we pick up two numbers in [2,9], the requirement for [1,10] can be achieved automatically.

# Finally we deal with the sorted intervals one by one.
# (1) If there is no number in this interval being chosen before, we pick up 2 biggest number in this interval. (the biggest number have the most possibility to be used by next interval)
# (2) If there is one number in this interval being chosen before, we pick up the biggest number in this interval.
# (3) If there are already two numbers in this interval being chosen before, we can skip this interval since the requirement has been fulfilled.

class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])  #sort on basis of upper limit
        size = 0
        start = -1
        end = -1
        for i in intervals:
            if end < i[0]:  # new interval is fully distinct from [start, end]
                end = i[1]
                start = i[1] - 1
                size = size + 2
            elif start < i[0]:  # partial overlap
                if end == i[1]:
                    start = end - 1
                else:
                    start = end
                end = i[1]
                size = size + 1
                              
        return size 
                
            
