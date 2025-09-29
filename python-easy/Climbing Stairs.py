# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.

class Solution:
 
    mem = {}
    def climbStairs(self, n: int) -> int:
        if n in self.mem:
            return self.mem[n]

        if n == 0:
            return 1
        if n < 0:
            # overstep: this is 0 valid ways
            return 0
        
        n2 = self.climbStairs(n - 2)
        self.mem[n-2] = n2
        n1 = self.climbStairs(n - 1)
        self.mem[n-1] = n1
        
        return n1+n2
