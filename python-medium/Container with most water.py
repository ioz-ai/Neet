# You are given an integer array heights where heights[i] represents the height of the 
# ithi'th bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l = 0
        r = len(heights) - 1
        while l < r:
            new_area = (r-l) * min(heights[l],heights[r])
            if new_area > max_area:
                max_area = new_area
            else:
                # Move the pointer associated with the shorter line
                # This is the correct, necessary move to maximize the chance
                # of finding a taller container.
                if heights[l] < heights[r]:
                    l += 1
                else:
                    # If heights are equal, move either one (or both);
                    # moving 'r' is a common convention when they are equal.
                    r -= 1
        return max_area
        