# 155. Min Stack
# Medium
# 11.6K
# 735
# Companies
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


# ````````````````````````````````


class MinStack:

    def __init__(self):
        self.arr = []
        self.min_val = 0
        self.min_arr = []

    def push(self, val: int) -> None:
        if not self.arr:
            self.arr.append(val)
            self.min_arr.append(val)
            self.min_val = val
            return
        self.arr.append(val)
        if val <= self.min_val:
            self.min_val = val
            self.min_arr.append(val)

    def pop(self) -> None:
        if self.min_val == self.arr.pop():
            self.min_arr.pop()
            if self.min_arr:
                self.min_val = self.min_arr[-1]

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
