# You are given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        left=0
        right = x//2
        sqrt_x = (left+right)//2
        while left <= right:
            mid = (left+right)//2
            mul = mid*mid
  
            if mul == x:  #exact
                return mid
            elif x < mul:
                sqrt_x = mid
                #lower
                right = mid - 1
                
            else:  # larger
                
                left = mid + 1

        if sqrt_x*sqrt_x > x:
            sqrt_x = sqrt_x - 1
    
        return sqrt_x