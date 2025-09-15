# You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.

# After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k