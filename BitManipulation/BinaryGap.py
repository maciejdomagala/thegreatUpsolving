"""
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. 
For example, the two 1's in "1001" have a distance of 3.
"""

class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxx, index = 0,0
        for i, bit in enumerate(bin(n)[2:]):
            if bit == '1':
                maxx = max(maxx, i - index)
                index = i
                
        return maxx
        