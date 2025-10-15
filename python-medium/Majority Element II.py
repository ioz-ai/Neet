# You are given an integer array nums of size n, find all elements that appear more than ⌊ n/3 ⌋ times. You can return the result in any order.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        n = len(nums)
        for i in nums:
            if i in counts.keys():
                counts[i] += 1
            else:
                counts[i] = 1
        
        res = []
        thr = n//3

        for k, v in counts.items():
            if v > thr:
                res.append(k)

        return res