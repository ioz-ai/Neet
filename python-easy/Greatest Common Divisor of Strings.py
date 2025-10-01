# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# You are given two strings str1 and str2, return the largest string x such that x divides both str1 and str2. If there is no such string, return "".
import math
class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Commutativity
        if str1 + str2 != str2 + str1:
            return ""
        
        len1 = len(str1)
        len2 = len(str2)
        
        # Calculate the length of the potential GCD string
        max_gcd_length = math.gcd(len1, len2)
        
        # Step 3: Return the substring of str1 with that length
        # Since str1 + str2 == str2 + str1, we know this substring works.
        return str1[:max_gcd_length]
 