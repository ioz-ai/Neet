# You are given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search, but the exit is if found or l and r are next to each other and smaller and larger

        l = 0
        r = len(nums)-1
        
        while l<=r:
            m = l+(r-l)//2
    
            if nums[m] == target:
                return m
            elif l == 0 and target <= nums[l]:
                return l
            elif r == len(nums)-1 and target > nums[r]:
                return r+1
            elif r == len(nums)-1 and target == nums[r]:
                return r
            elif r-l == 1 and nums[l]<target and nums[r]>target:
                return r
            elif nums[m] < target:
                l = m
            else: # nums[m] > target
                r = m
        return -1
