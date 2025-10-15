# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            # Format: [length]#[string]
            # Use ':' or '/' as the delimiter is common, but '#' is simple here.
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0  # Pointer for the encoded string
        
        while i < len(s):
            # 1. Find the delimiter '#' to separate length from string
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            
            # 2. Extract and parse the length (substring from i to j)
            # This handles numbers of any length (e.g., "10#", "100#")
            length = int(s[i:j])
            
            # 3. Calculate start index of the actual string
            # Start is immediately after the delimiter (#)
            start_index = j + 1
            
            # 4. Extract the string using the calculated length
            end_index = start_index + length
            current_string = s[start_index:end_index]
            
            # 5. Append to result and advance pointer to the start of the next prefix
            decoded_list.append(current_string)
            i = end_index
            
        return decoded_list