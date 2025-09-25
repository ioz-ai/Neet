# Given a binary tree, return true if it is height-balanced and false otherwise.

# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

class Solution:
    def digitSum(self, n: int) -> int:
        sum_n = 0
        while n > 0:
            digit = n % 10
            sum_n += digit*digit
            n = n//10
        return sum_n

    def isHappy(self, n: int) -> bool:
        # maintain a sum set for bouncing numbers
        m = set()
        for i in range(100):
            sum_n = self.digitSum(n)
            if sum_n == 1:
                return True
            
            n = sum_n
            if n in m:
                break
            else:
                m.add(n)

        if sum_n == 1:
            return True

        return False