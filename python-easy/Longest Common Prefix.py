# You are given an array of strings strs. Return the longest common prefix of all the strings.

# If there is no longest common prefix, return an empty string "".
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i, char in enumerate(strs[0]):
            for other_string in strs[1:]:
                if i == len(other_string) or other_string[i] != char:
                    return strs[0][:i]
        return strs[0]