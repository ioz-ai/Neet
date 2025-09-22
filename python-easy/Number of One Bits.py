# You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

# You may assume n is a non-negative integer which fits within 32-bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += (n & 1)
            n = n >> 1
        return count