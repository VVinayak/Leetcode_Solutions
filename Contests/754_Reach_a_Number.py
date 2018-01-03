#73 / 73 test cases passed.

#Runtime: 32 ms

# The fastest way to get close to (not equal to) the target is keeping adding until we get right bigger than target. Let's call it sum_till_n, which is sum([i for i in range(n+1)]).
# After we get the smallest sum_till_n that is larger than target, we want to subtract the rest (sum_till_n-target) so that we can get back to target
# For any i we added to sum_till_n, if we flip the +i to -i, we are subtracting 2i from sum_till_n
# We can see, there is no odd number for us to subtract by flipping + to -. We increment till we get an even number difference
# There is no change in the number of steps by simply flipping the positive to negative numbers

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """  
        t = abs(target)
        n = math.floor(0.5*(-1 + math.sqrt(1 + 8*t)))
        # finding nearest n by solving n*(n+1)/2 = t
        while True:
            difference = (n*(n+1))/2 - t
            if difference>=0:
                if difference%2 == 0:
                    return int(n)
            n = n + 1   # if the difference is not positive or is odd, increment n
