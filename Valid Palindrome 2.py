# You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.
# A palindrome is a string that reads the same forward and backward.
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

class Solution:
    def validPalindrome(self, s: str) -> bool:

        for i in range(len(s)):
            if i == len(s):
                if checkF(s):
                    return True
            else:
                #derive a substring
                sub = s[0:i]+s[i+1:]
                if checkF(sub):
                    return True

        return False

def checkF(s: str) -> bool:
    m = math.floor(len(s)/2)
    for i in range(m):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
