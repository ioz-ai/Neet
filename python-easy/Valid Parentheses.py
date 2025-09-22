# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string of brackets is valid.

        Args:
          s: A string consisting of '(', ')', '{', '}', '[' and ']'.

        Returns:
          True if the string is valid, and False otherwise.
        """
        # A stack to keep track of opening brackets.
        stack = []

        # A mapping of closing brackets to their corresponding opening brackets.
        closeToOpen = {")": "(", "}": "{", "]": "["}

        # Iterate through each character in the string.
        for char in s:
            # If the character is a closing bracket...
            if char in closeToOpen:
                # Check if the stack is not empty and the top of the stack
                # is the matching opening bracket.
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()  # It's a match, so pop the opening bracket.
                else:
                    return False  # Mismatch or no opening bracket.
            # If the character is an opening bracket...
            else:
                stack.append(char) # Push it onto the stack.

        # If the stack is empty, all brackets were matched correctly.
        # Otherwise, there are unclosed opening brackets.
        return True if not stack else False
