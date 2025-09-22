# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.

from collections import deque

class MyStack:

    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()

    def push(self, x: int) -> None:
        
        actual = self.que1
        if len(self.que2) > 0:
            actual = self.que2
        #print("pre push", actual)
        actual.append(x)
        #print("post push", actual)


    def pop(self) -> int:
        # while fr is full
        # popleft and add it to to
        # return the last element 
        fr = self.que1
        to = self.que2
        if len(self.que2) > 0:
            fr = self.que2
            to = self.que1
        
        el = fr[0]
        while len(fr) > 1:
            el = fr[0]
            to.append(fr[0])
            fr.popleft()
        el = fr[0]
        fr.popleft()
        return el

        

    def top(self) -> int:
        actual = self.que1
        if len(self.que2) > 0:
            actual = self.que2
        print("top", actual[-1])
        return actual[-1]
        

    def empty(self) -> bool: 
        return (not(self.que1) or len(self.que1)==0) and (not(self.que2) or len(self.que2) == 0)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()