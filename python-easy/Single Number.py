# You are given a non-empty array of integers nums. Every integer appears twice except for one.

# Return the integer that appears only once.

# You must implement a solution with O(n) runtime complexity and use only O(1) extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        # Iterate through each number in the list.
        for num in nums:
            # XOR the current result with the current number.
            result ^= num

            
        # The final result is the single number.
        return result