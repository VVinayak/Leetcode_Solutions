#51 / 51 test cases passed.

#Runtime: 52 ms

#  Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.

# We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

# These lists A and B may contain duplicates. If there are multiple answers, output any of them. 

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result = [0]*(len(A))
        for i in xrange(len(A)):
            if A[i] in B:
                result[i] = B.index(A[i])
                
        return result
