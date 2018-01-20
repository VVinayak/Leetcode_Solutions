#86 / 86 test cases passed.

#Runtime: 38 ms

#  Special binary strings are binary strings with the following two properties:

# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.

# Given a special string S, a move consists of choosing two consecutive, non-empty, special substrings of S, and swapping them. (Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)

# At the end of any number of moves, what is the lexicographically largest resulting string possible? 

#-------------------------------------------------------------------------------------------------------------------------------------------

# Just 4 steps:

#     Split S into several special strings (as many as possible).
#     Special string starts with 1 and ends with 0. Recursion on the middle part.
#     Sort all special strings in lexicographically largest order.
#     Join and output all strings.

# Updated:

# The middle part of a special string may not be another special string. But in my recursion it is.
# For example, 1M0 is a splitted special string. M is its middle part and it must be another special string.

# Because:

#     The number of 0's is equal to the number of 1's in M
#     If there is a prefix P of Mwhich has one less 1's than 0's, 1P will make up a special string. 1P will be found as special string before 1M0 in my solution.
#     It means that every prefix of M has at least as many 1's as 0's.

# Based on 2 points above, M is a special string.
#---------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = i = 0
        res = []
        for j,digit in enumerate(S):
            if digit == '1':
                count = count + 1
            else:
                count = count - 1
            if count == 0:
                res.append('1'+self.makeLargestSpecial(S[i+1:j])+'0')
                i = j + 1
        
        return ''.join(sorted(res)[::-1])
