# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items = {}
        for i in nums:
            if i in items:
                return True
            items[i] = 1
        return False