# Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.
# Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=sum(nums)
        n=len(nums)
        e=(n+1)*(n)//2

        return e-s