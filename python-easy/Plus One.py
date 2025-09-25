# You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

# Return the digits of the given integer after incrementing it by one.
from typing import List

class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = "".join(map(str, digits))

        num = int(num_str) + 1

        return [int(digit) for digit in str(num)]


