# You are given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        # 1. Divide (Find the middle and recursively sort halves)
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        # Recursively sort the halves
        left_half = self.sortArray(left_half)
        right_half = self.sortArray(right_half)
        
        # 2. Conquer (Merge the sorted halves)
        return self._merge(left_half, right_half)

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        # Merges two sorted lists into a single sorted list.
        merged = []
        i = j = 0  # Pointers for the left and right lists
        
        # Compare elements from both lists and append the smaller one
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        # Append any remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged