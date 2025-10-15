
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
from typing import List

class Solution:
    def get_key(self, str1: str) -> str:
        k = ""
        s=[]
        for i in str1:
            s.append(i)
        
        return "".join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        # create a hash key and group them based on the key
        for i in strs:
            k = self.get_key(i)
            
            if k in d:
                d[k].append(i)
            else:
                d[k]=[i]

        result =[]
        for k,v in d.items():
            result.append(v)
        return result