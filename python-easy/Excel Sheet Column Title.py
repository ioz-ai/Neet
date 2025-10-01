# You are given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.



class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        result = ""
        # run till dividend is 0
        while columnNumber > 0:
            #  1-based indexing (A=1) = (columnNumber - 1)
            
            # The remainder (0-25) = the index of the letter
            remainder_index = (columnNumber - 1) % 26
            # Append the character corresponding to the remainder index
            result = let[remainder_index] + result

            # The new columnNumber for the next iteration (the quotient)
            columnNumber = (columnNumber - 1) // 26
            
        return result
        