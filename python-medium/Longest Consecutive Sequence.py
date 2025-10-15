# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = {}

        for i in range(len(nums)):
            s[nums[i]]=1
        items = sorted(s.keys())

        if len(items) < 2:
            return len(items)

        max_len = 1  # start with 1, because minimum 1 length
        for i in range(len(items)-1):
            list_len = 1  # local length tracker
            j = i+1
            while j < len(items):
                if items[j] > items[i]+1:
                    i=j
                    break
                elif items[j] == items[i]+1:
                    i += 1
                    j += 1
                    list_len += 1

            if list_len > max_len:
                max_len = list_len

        return max_len

