#200 / 200 test cases passed.

#Runtime: 322 ms

#  Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

# (Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.) 
    # L, R will be integers L <= R in the range [1, 10^6].
    # R - L will be at most 10000.


class Solution(object):
    # def isPrime(self, count):
    #     if count<2:
    #         return False
    #     else:
    #         for i in xrange(2,(count/2)+1):
    #             if count%i != 0:
    #                 continue
    #             else:
    #                 return False
    #         return True
        
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        #only 20 digits in 10000 at worst so its better to just enumerate all primes till 20
        primes = [2,3,5,7,11,13,17,19,23]
        count = 0 
        for i in xrange(L, R+1):
            # print bin(i)
            if bin(i)[2:].count('1') in primes:
                count = count+1
                
        return count
