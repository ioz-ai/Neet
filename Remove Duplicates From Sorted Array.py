# You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.

# After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

# The order of the unique elements should remain the same as in the original array.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain all the unique elements.
# Return k as the final result.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 'i' is the slow-runner pointer, tracking the position of the last unique element.
        i = 0
        
        # 'j' is the fast-runner pointer, iterating through the list.
        for j in range(1, len(nums)):
            # If we find a new unique element...
            if nums[j] != nums[i]:
                # ...we increment 'i' to the next position...
                i += 1
                # ...and place the unique element there.
                nums[i] = nums[j]
        
        # The number of unique elements is i + 1.
        return i + 1
