#94 / 94 test cases passed.

#Runtime: 2046 ms

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindromelist = []
        if len(s)>1:
            for i in xrange(len(s)):
                palindromelist.append(self.checkpalindromes(s,i,i))  #odd length of palindrome
                palindromelist.append(self.checkpalindromes(s,i,i+1))  #even length of palindromes
            return max([p for p in palindromelist if p and p == p[::-1]], key=len)
        else:
            return s
            
    def checkpalindromes(self, string, leftindex, rightindex):
        while leftindex >= 0 and rightindex < len(string) and len(string)<=1000 and string[leftindex]==string[rightindex]:
            leftindex = leftindex - 1
            rightindex = rightindex + 1
        
        if leftindex < 0 or rightindex >= len(string):
            return string[leftindex+1:rightindex]
        elif string[leftindex]==string[rightindex]:
            return string[leftindex:rightindex+1]
        else:
            return string[leftindex+1:rightindex]
