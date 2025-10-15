# You are given an array nums consisting of n elements where each element is an integer representing a color:

# 0 represents red
# 1 represents white
# 2 represents blue
# Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

# You must not use any built-in sorting functions to solve this problem.
from typing import List

class Solution:
    def enhanced_swap(self, nums: List[int], target:int, start:int) -> int:
        if start >= len(nums):
            return len(nums)
        
        # 'current_index' tracks where the next 'target' element should be placed.
        # This pointer starts at the beginning of the subarray.
        current_index = start
        
        # Iterate through the subarray from 'start' to the end.
        for i in range(start, len(nums)):
            # If we find the target number, swap it with the element at current_index.
            if nums[i] == target:
                # Swap nums[i] (the target) with nums[current_index]
                nums[i], nums[current_index] = nums[current_index], nums[i]
                
                # Advance the placement pointer
                current_index += 1
                
        # current_index now points to the first index *after* all 'target' elements
        return current_index

    def sortColors(self, nums: List[int]) -> None:
        # swap
        end_index = self.enhanced_swap(nums, 0, 0)
        end_index = self.enhanced_swap(nums, 1, end_index)
        end_index = self.enhanced_swap(nums, 2, end_index)
 