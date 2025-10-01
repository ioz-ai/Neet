# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

# You may choose to start at the index 0 or the index 1 floor.

# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.
from typing import List, Dict

class Solution:
    mem: Dict[int, int] = {}

    def CostClimbingStairs(self, n: int, cost: List[int]) -> int:
        if n in self.mem:
            return self.mem[n]

        # 1. Base Case: the "top"
        if n >= len(cost):
            return 0
    
        # 2. Recursive Step:
        # Cost to leave the current step (cost[n]) + 
        # min cost from taking one step OR taking two steps.
        
        # Cost of 1 step: cost[n] + rec(n+1)
        cost_one_step = cost[n] + self.CostClimbingStairs(n + 1, cost)
        
        # Cost of 2 steps: cost[n] + rec(n+2)
        cost_two_steps = cost[n] + self.CostClimbingStairs(n + 2, cost)

        result = min(cost_one_step, cost_two_steps)
        self.mem[n] = result
        return result


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.mem = {}
        
        # The answer is the minimum cost to reach the top, starting from index 0 OR index 1.
        return min(self.CostClimbingStairs(0, cost), self.CostClimbingStairs(1, cost))
        