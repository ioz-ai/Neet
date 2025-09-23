# You are given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        i = len(a)-1
        j = len(b)-1
        
        carry = 0
        while i >= 0 or j >= 0:
            if (i >= 0) and (j >= 0) :
                s = carry + int(a[i]) + int(b[j])
            elif (i >= 0):
                s = carry + int(a[i])
            else:
                s = carry + int(b[j])
            
            i=i-1
            j=j-1
            if s >= 2:
                carry = 1
                s = s - 2
            else:
                carry = 0
            result = str(s) + result
            
        if carry > 0:
            result="1"+result
       
        return result
        