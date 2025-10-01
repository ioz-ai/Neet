# You are given a row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1.

# Return the perimeter of the island.
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        c = 0
        C = len(grid[0])
        R = len(grid)
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    c += 4
                    # Check Top Neighbor
                    if i > 0 and grid[i-1][j] == 1:
                        c -= 1
                        
                    # Bottom Neighbor 
                    if i < R - 1 and grid[i+1][j] == 1:
                        c -= 1
                        
                    # Check Left Neighbor
                    if j > 0 and grid[i][j-1] == 1:
                        c -= 1
                        
                    # Check Right Neighbor
                    if j < C - 1 and grid[i][j+1] == 1:
                        c -= 1

        return c