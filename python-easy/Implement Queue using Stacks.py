# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.


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