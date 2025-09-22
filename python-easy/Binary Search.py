# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in O(logn) time.

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) -1
        m = math.floor((l+r)/2)
        
        while l<=r:
            
            if nums[m] == target:
                return m
            else:
                
                if target < nums[m]:
                    r=m-1
                    m=math.floor((l+r)/2)
                elif target > nums[m]:
                    l=m+1
                    m=math.floor((l+r)/2)
                
        return -1
