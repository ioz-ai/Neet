# You are given an array of characters which represents a string s. Write a function which reverses a string.

# You must do this by modifying the input array in-place with O(1) extra memory.
from typing import List
import math

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        m = math.floor(len(s)/2)

        print(s, m)
        for i in range(0,m):
            
            temp = s[i]
            sec = len(s)-1-i
           
            s[i]=s[sec]
            s[sec] = temp