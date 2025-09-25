# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# You are given an array nums, return the sum of all XOR totals for every subset of nums.

# Note: Subsets with the same elements should be counted multiple times.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Calculates the sum of XOR totals for every subset of nums.
    
        This solution uses a mathematical shortcut for an O(n) result.
        """
        n = len(nums)
    
        # If the list is empty, there are no subsets.
        if n == 0:
            return 0
        
        # 1. Calculate the bitwise OR of all numbers in the array.
        or_total = 0
        for num in nums:
            or_total |= num
        
        # 2. The final result is the OR total multiplied by 2^(n-1).
        # We can use a left bit shift (<<) for the power of 2 calculation.
        return or_total * (1 << (n - 1))
123
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        








