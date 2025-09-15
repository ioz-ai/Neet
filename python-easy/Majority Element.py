# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = {}

        for i in range(len(nums)):
            if nums[i] in c:
                c[nums[i]] = c[nums[i]] + 1
            else:
                c[nums[i]] = 1
        
        for k, v in c.items():
            if v > len(nums) / 2:
                return k

        return -1