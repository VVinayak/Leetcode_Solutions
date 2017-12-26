#19 / 19 test cases passed.
#Runtime: 618 ms

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i in xrange(len(nums)):
            table[i] = nums[i]
            complement =  target - nums[i]
            if complement in table.values() and table.keys()[table.values().index(complement)] != i:
                result = [i, table.keys()[table.values().index(complement)]]
                return result
                
             
