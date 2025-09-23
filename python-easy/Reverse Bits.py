# Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0

        for i in range(32):
            # Left-shift the reversed number to make space for the next bit
            reversed_n <<= 1
            str = "reversed_n " + bin(reversed_n)
            
            # Get the last bit of n and add it to reversed_n
            # Use bitwise OR to append the bit
            reversed_n |= (n & 1)
            
            # Right-shift n to process the next bit
            n >>= 1

        return reversed_n