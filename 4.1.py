"""
Implement a stack with push, pop, and max
Max peeks at greatest value, not top value
"""
import sys

class Stack: 
    def __init__(self):
        self.arr = []
        self.max_stack = []
        self.count = 0
    def push(self, val):
        self.arr.append(val)
        if self.count == 0 or val > self.max_stack[-1]:
            self.max_stack.append(val)
        else:
            self.max_stack.append(self.max_stack[-1])
        self.count+=1
    def pop(self):
        if self.count == 0:
            raise Exception("Cannot pop empty stack")
        self.count-=1
        self.max_stack.pop()
        return self.arr.pop()
    def max(self):
        if self.count == 0:
            raise Exception("Cannot max empty stack")
        return self.max_stack[-1]

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.max())
print(s.pop())
print(s.max())
