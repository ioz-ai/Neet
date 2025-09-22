# You are given an integer array nums and an integer k, return true if there are 
# two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k,
#  otherwise return false.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {}

        # Enumerate through the list to get both the index and the value.
        for i in range(len(nums)):
            num = nums[i]
            # Check if the number is already in our map.
            if num in num_map:
                # If it is, check if the distance between the current index 'i'
                # and the last seen index is less than or equal to k.
                if i - num_map[num] <= k:
                    return True
            
            # Whether the number was a duplicate or not, update the map
            # with the current (most recent) index.
            num_map[num] = i
        
        # If we finish the loop without finding a valid pair, return False.
        return False