# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3 or (len(nums)==3 and sum(nums)!= 0):
            return []
        nums.sort()

        result = {}

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for z in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[z] == 0:
                        result[nums[i], nums[j], nums[z]]=1

        return list(result.keys())