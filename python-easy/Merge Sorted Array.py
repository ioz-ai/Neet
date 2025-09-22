# You are given two integer arrays nums1 and nums2, both sorted in non-decreasing order, along with two integers m and n, where:

# m is the number of valid elements in nums1,
# n is the number of elements in nums2.
# The array nums1 has a total length of (m+n), with the first m elements containing the values to be merged, and the last n elements set to 0 as placeholders.

# Your task is to merge the two arrays such that the final merged array is also sorted in non-decreasing order and stored entirely within nums1.
# You must modify nums1 in-place and do not return anything from the function.
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1  # Pointer for nums1's valid elements
        j = n-1  # Pointer for nums2
        w = m+n-1  # Pointer for the write position in nums1

        # Merge the two arrays by comparing elements from the end
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[w] = nums1[i]
                i -= 1
            else:
                nums1[w] = nums2[j]
                j -= 1
            w -= 1

        # If there are any remaining elements in nums2, copy them
        # to the beginning of nums1.
        while j >= 0:
            nums1[w] = nums2[j]
            j -= 1
            w -= 1
