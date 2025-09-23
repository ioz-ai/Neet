# Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

# Return an array output where output[i] is the number of 1's in the binary representation of i.

class Solution:
    def num_ones(self, n: int) -> int:
        count = 0
        while n > 0:
            count += (n & 1)
            n = n >> 1
        return count

    def countBits(self, n: int) -> List[int]:
        result = [0]*(n+1)
        
        for i in range(0, n+1):
            result[i] = self.num_ones(i)
            
        return result