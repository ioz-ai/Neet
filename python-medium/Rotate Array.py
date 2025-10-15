
# You are given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) == 0:
            return
        k %= len(nums)
        # save the last element index
        last_i = len(nums)-1
        for i in range(k):
            # the last element
            last_el = nums[last_i]
            for j in range(last_i, -1, -1):
                nums[j]=nums[j-1]
            # copy to the front
            nums[0]=last_el
            
                