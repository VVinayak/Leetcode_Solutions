#983 / 983 test cases passed.

#Runtime: 122 ms

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length_of_substrings = [0]
        substring = []
        substring_indices = {}
        alphabets = list(s)
        if list(s):
            for i in xrange(len(alphabets)):
                if alphabets[i] in substring:
                    length_of_substrings.append(len(substring))
                    substring = alphabets[(substring_indices[alphabets[i]]+1):(i+1)]     # emptying substring and keeping only non-repeating elements in it
                else:
                    substring.append(alphabets[i])
                    
                substring_indices[alphabets[i]] = i
                
            #appending the last unique sequence
            length_of_substrings.append(len(substring))
                
        return max(length_of_substrings) 
