# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l = len(s)
        c=''
        for i in s:
            if (i <= 'z' and i >='a') or (i <= '9' and i >='0'):
                c=c+i
        l = len(c)
        print(c)
        if l==1:
            return True

        h=math.floor(l/2)
 
        for i in range(0, h):
            print(i)
            if i==l-1-i:
                break
            
            if c[i] != c[l-1-i]:
                return False

        return True
        