"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        fav = nums[0]
        for a in nums:
            if count == 0:
                fav = a         
            
            if a == fav:
                count += 1
            else:
                count -= 1
                
        return fav