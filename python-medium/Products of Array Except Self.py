# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l2r = [1]*n
        r2l = l2r.copy()

        for i in range(n):
            if i == 0:
                l2r[0]=nums[i]
            else:
                l2r[i] = l2r[i-1]*nums[i]
        
        for i in range(n-1,-1,-1):
            if i == n-1:
                r2l[i]=nums[n-1]
            else:
                r2l[i]=r2l[i+1]*nums[i]

        result=[1]*n
        for i in range(len(nums)):
            if i == 0:
                result[i] = r2l[i+1]
            elif i == n-1:
                result[i] = l2r[i-1]
            else:
                result[i] = l2r[i-1]*r2l[i+1]

        return result
