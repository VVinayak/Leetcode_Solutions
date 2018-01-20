#116 / 116 test cases passed.
#Runtime: 89 ms

# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts. 


#     S will have length in range [1, 500].
#     S will consist of lowercase letters ('a' to 'z') only.


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lengths = []
        i = 0
        start = stop = 0
        for i in xrange(len(S)):
            if start <= i and i <= stop:
                # print S[::-1].index(S[i])
                if stop < len(S) -1 - S[::-1].index(S[i]):
                    stop = len(S) -1 - S[::-1].index(S[i]) 
                    #finding last position of element and assigning it to stop if the first position of element is in between [start, stop]   
            elif stop < i:
                #when first position of element is beyond the stop position, one substring is ready
                lengths.append(stop - start + 1)
                start = i
                stop = len(S) -1 - S[::-1].index(S[i])
                
        lengths.append(stop - start + 1)      
        return lengths
