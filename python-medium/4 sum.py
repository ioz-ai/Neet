
# You are given an integer array nums of size n, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Note: [1,0,3,2] and [3,0,1,2] are considered as same quadruplets.

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 1. Sort the list first (This is essential for the two-pointer method and duplicate skipping)
        nums.sort()
        n = len(nums)
        res = []

        # Outer loop fixes the first element (i)
        for i in range(n - 3):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Second loop fixes the second element (j)
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # 2. Two-Pointer setup for the remaining two elements
                left, right = j + 1, n - 1
                
                # Correctly calculate the remaining target sum
                remaining_target_sum = target - nums[i] - nums[j]

                while left < right:
                    current_sum = nums[left] + nums[right]

                    if current_sum == remaining_target_sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Found a solution, move pointers
                        left += 1
                        right -= 1
                        
                        # SKIP DUPLICATES for left and right pointers
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif current_sum < remaining_target_sum:
                        left += 1
                    else: # current_sum > remaining_target_sum
                        right -= 1
                        
        return res