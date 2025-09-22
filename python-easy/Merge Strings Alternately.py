# You are given two strings, word1 and word2. Construct a new string by merging them in alternating order, starting with word1 — take one character from word1, then one from word2, and repeat this process.
# If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result.
# Return the final merged string

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        result = ""
       
        while i < len(word1) or j < len(word2):
            
            if i < len(word1):
                result = result + word1[i]
                i = i + 1
           
            if j  < len(word2):
                result = result + word2[j]
                j = j + 1
           

        return result
            