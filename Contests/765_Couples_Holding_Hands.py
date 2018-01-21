#56 / 56 test cases passed.

#Runtime: 433 ms

#  N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

# The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

# The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat. 


#---------------------------------------------------------------------------------------------------------------------------------------------------

# if a number is even, we need to search for the number+1. And we swap it to an odd location 1 more than number's index if number is in an even index location (or we swap number+1 to an even location 1 less than the index of number if number's index is odd ). if a number is odd, we search for number-1. And we swap it to an odd location 1 more than number's index if number is in an even index location (or we swap number+1 to an even location 1 less than the index of number if number's index is odd ). Edge cases are when we are at the first and last index of the array

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        swaps = 0
        for i,value in enumerate(row):
            print i,value,row
            if value%2 == 0:
                if i == 0 and value+1 !=row[i+1]:
                    swaps = swaps + 1
                    temp1 = row.index(value+1)
                    temp2 = row[1]
                    row[1] = row[temp1]
                    row[temp1] = temp2
                elif i==len(row)-1 and value+1 !=row[i-1]:
                    swaps = swaps + 1
                    temp1 = row.index(value+1)
                    temp2 = row[i-1]
                    row[i-1] = row[temp1]
                    row[temp1] = temp2
                elif i+1<len(row) and i-1>=0 and (value+1 !=row[i+1] and value+1 != row[i-1]):
                    swaps = swaps + 1
                    temp1 = row.index(value+1)
                    if (i%2!=0) or (i-2<0):
                        temp2 = row[i-1]
                        row[i-1] = row[temp1]
                        row[temp1] = temp2
                    if (i%2==0) or (i+2>len(row)):
                        temp2 = row[i+1]
                        row[i+1] = row[temp1]
                        row[temp1] = temp2            
            else:
                if i == 0 and value-1 !=row[i+1]:
                    swaps = swaps + 1
                    temp1 = row.index(value-1)
                    temp2 = row[1]
                    row[1] = row[temp1]
                    row[temp1] = temp2
                elif i==len(row)-1 and value-1 !=row[i-1]:
                    swaps = swaps + 1
                    temp1 = row.index(value-1)
                    temp2 = row[i-1]
                    row[i-1] = row[temp1]
                    row[temp1] = temp2
                if i+1<len(row) and i-1>=0 and (value-1 !=row[i+1] and value-1 != row[i-1]):
                    swaps = swaps + 1
                    temp1 = row.index(value-1)
                    if (i%2!=0) or (i-2<0):
                        temp2 = row[i-1]
                        row[i-1] = row[temp1]
                        row[temp1] = temp2
                    if (i%2==0) or (i+2>len(row)):
                        temp2 = row[i+1]
                        row[i+1] = row[temp1]
                        row[temp1] = temp2
                    
        return swaps
